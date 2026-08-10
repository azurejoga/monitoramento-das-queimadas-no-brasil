# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff2b09d4-ac10-3fab-b0f9-c96aa94cc592 | -13.84336 | -53.89463 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbe0767b-dea4-3781-ada8-4f0a4b85ac39 | -9.06963 | -65.46162 | 2026-08-10 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc72cc3f-e297-3117-9494-74fc3537f7fd | -10.0733 | -60.50135 | 2026-08-10 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63f4abb-b753-322d-98f2-72f95a3f6636 | -15.15615 | -52.71852 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c14aa32-10f0-3738-8f37-3e620d6a8b7e | -15.15111 | -52.7179 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 96b993a7-6475-3b19-8bd8-466a9ddc0ec1 | -11.8427 | -56.94812 | 2026-08-10 05:29:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f938fe2-36d4-34e0-96ee-a05a183d2477 | -11.62373 | -51.09555 | 2026-08-10 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a75cdf5f-5b47-31b8-a17c-2c3ac9b8c8fe | -15.15237 | -52.71252 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| eddfc660-d077-3f03-974e-06bbc18eab6d | -8.68524 | -62.86904 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbefa8eb-aff4-344d-876b-47248d2333e6 | -11.99524 | -60.51178 | 2026-08-10 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3915bf34-1da1-3c0d-aa28-f9ae4f1ae7d6 | -10.93727 | -57.11134 | 2026-08-10 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50506c3c-93a5-3936-b779-3a1eadd38f10 | -13.84925 | -53.67846 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a097edc1-7734-3ce6-8e67-f907b782eee2 | -11.6265 | -51.09336 | 2026-08-10 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 645a682a-2b03-3b0b-80af-fb53e76cbb8a | -14.14074 | -54.00686 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 11acff89-e13d-3da8-91c1-b037eca0095e | -11.21256 | -54.02738 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73194b60-a58c-3696-af13-324d2bf64418 | -13.95341 | -58.09792 | 2026-08-10 05:29:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5278abad-9955-398c-a25a-fb512fc1a5b0 | -16.06027 | -50.80193 | 2026-08-10 05:29:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72614035-ef58-3190-8b3d-b194febadca4 | -14.13559 | -54.01095 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b4826beb-f2a9-3691-b0f6-f9b10ce32bdb | -15.84771 | -48.13176 | 2026-08-10 05:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d980408c-2201-3ea5-8389-70fae6336174 | -13.84664 | -53.69803 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0691f7f5-ccb4-3b33-a0e5-b21f8586eb32 | -13.86348 | -53.66196 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95692e58-e567-36ea-b1cd-b3ba8b4c5f7f | -8.68887 | -62.86965 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6926428f-d338-3ae7-a813-665d930466eb | -14.13339 | -54.02192 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f9a6695-4ad4-34fa-8ffc-1ee6abd8f5b5 | -14.13463 | -54.0127 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 47e02598-8ff2-3f42-b259-f53de6c28a08 | -15.15311 | -52.70661 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c8c87cfb-7772-3fc6-8582-d9c844c95f1a | -16.06075 | -50.79761 | 2026-08-10 05:29:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4d39d3b7-dbe6-31a5-9f61-1d7be239da1d | -15.14806 | -52.70604 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15fd0c15-8904-30ed-ba4e-a02e35ea9b46 | -10.90643 | -56.36981 | 2026-08-10 05:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2593f95b-78b3-30fd-8dbd-d19fc2464354 | -8.6423 | -63.62005 | 2026-08-10 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27e41a8b-e9cf-3e59-81ee-20d7c97c5565 | -8.68761 | -62.87537 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a29a63f5-8e20-36dc-a6a9-6812e7dcdb8e | -13.84728 | -53.69322 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49c434da-3281-343b-9645-1d1d6508897e | -8.68468 | -62.87052 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1d5155a-49f1-3467-b4ee-bd8ff920302c | -10.07663 | -60.50189 | 2026-08-10 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f87c30-3a8c-34b4-9e43-c7689db7f0c0 | -15.36881 | -53.76736 | 2026-08-10 05:29:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f91080e-e9c2-34eb-936d-13b7f3549d28 | -13.95695 | -58.09847 | 2026-08-10 05:29:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f269228a-aa8f-30d3-a664-c82c4f1d6284 | -11.47434 | -50.55632 | 2026-08-10 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94635d0-ac99-340d-bd86-251a3a9debac | -15.15672 | -52.71865 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7710e219-45dd-32e7-b817-0062f9e253ae | -8.68398 | -62.87476 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5b28998-651a-3a69-9fe7-4694fdc7be43 | -14.13401 | -54.01733 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b8f32ed2-72f9-3043-9efc-23e8bdea8319 | -14.135 | -54.01562 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fdcab7ba-f287-39c5-b630-69de15124ae6 | -13.9528 | -58.10202 | 2026-08-10 05:29:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2accae7b-37c9-3077-8764-8a3d121b68bf | -14.12545 | -53.97726 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64ded97c-4ec6-3758-9340-b16d9ae0ce73 | -13.85649 | -53.69488 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e58f3494-9f36-3ee3-87be-74d8da1c7700 | -12.09113 | -47.20314 | 2026-08-10 05:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a37e51e6-1876-3485-8a6b-1bc5eadea26b | -8.68744 | -62.8781 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f82617a1-8d05-3ae1-836c-72ecada990ff | -13.85716 | -53.68983 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62265595-74d9-3ac5-bc75-f025565c5a37 | -11.21573 | -54.03643 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 042c2a73-eeb5-340a-8df2-90e6c3213a08 | -13.86113 | -53.66013 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c209d08a-8d53-3cf5-ade5-67b3fdb39de0 | -8.68329 | -62.87899 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 039776ef-0a3b-3458-a60e-083afa3001ac | -11.22009 | -54.037 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57e2703f-dc75-32a9-962a-a005198e7f00 | -11.21632 | -54.03218 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4454f750-1f54-3ba7-a7d0-a821b8d39d2e | -13.86409 | -53.65709 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53fc3a5f-213a-312f-a4cf-88a481d56571 | -11.81588 | -63.03898 | 2026-08-10 05:29:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6235d1a0-4480-3b63-81a3-fa9877839e73 | -15.9761 | -54.21618 | 2026-08-10 05:29:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccfe030f-7e6f-30f6-bbd9-21683cafb1e7 | -16.06652 | -50.79842 | 2026-08-10 05:29:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9377b32f-c502-3924-80c8-cf6c48aec3ac | -14.30127 | -54.9313 | 2026-08-10 05:29:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64535da8-78f9-3266-9e46-94ebeab27ae4 | -9.04946 | -60.38595 | 2026-08-10 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56f8e767-a60c-3a03-bb4a-8fe399b56912 | -11.62115 | -51.09262 | 2026-08-10 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2350bea-8a28-3816-8ed0-c1b244765efe | -11.46836 | -50.55926 | 2026-08-10 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93586145-d463-3a51-81ac-e68fe264fa68 | -11.4739 | -50.56 | 2026-08-10 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4551ce26-b4ab-3b1f-8992-d847b9ddcdec | -13.95635 | -58.10256 | 2026-08-10 05:29:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 337019c4-84be-3077-a332-434c0336a3c4 | -11.17221 | -54.80386 | 2026-08-10 05:29:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bdcdaeb-1395-33f4-8f5e-3757977bb267 | -11.62156 | -51.08921 | 2026-08-10 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4531a5c2-0bcc-3649-852a-97d75ac04ae7 | -15.13806 | -52.69816 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 702b3fa0-a18b-3235-9b4c-b825bce1d2bb | -11.62418 | -51.09215 | 2026-08-10 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40ba30df-f1a0-3a9c-82a8-01816e2961d6 | -11.21196 | -54.03162 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae6726db-8f68-3451-9db4-7e973ac6e558 | -11.46979 | -50.55717 | 2026-08-10 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a06ea9-0cbd-3d27-a1ec-ae248e756d95 | -11.21692 | -54.02793 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f71d47d3-fe7f-33a6-b038-0baa9f8bece6 | -10.93665 | -57.11555 | 2026-08-10 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9881d229-b893-3b61-84fb-3994a9924893 | -10.93603 | -57.11974 | 2026-08-10 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1ca8a76-8d3f-3048-a812-e8ecbb21de80 | -11.2076 | -54.03104 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 360bf322-49ac-3bd1-953b-433c78dd5a09 | -13.85945 | -58.17615 | 2026-08-10 05:29:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d83471d-e5d8-38bf-88f6-09dcd312c410 | -20.88379 | -57.70704 | 2026-08-10 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 514422f8-616f-37fd-9573-4ed1ee443889 | -16.49358 | -54.65329 | 2026-08-10 05:31:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21096489-47c8-3a6a-83c6-3988cfe36e31 | -16.49807 | -54.65404 | 2026-08-10 05:31:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c205b30-bf0a-3325-9211-ed3e1d0f9a79 | -16.4926 | -54.65165 | 2026-08-10 05:31:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1112d6d6-fa51-357f-91a6-2bf67fbc13ee | -20.87592 | -57.70588 | 2026-08-10 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| daf6c5db-a264-3c66-8adb-bbfc96f43368 | -20.785 | -57.67503 | 2026-08-10 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a469eecf-a665-3e4a-87e3-99fd865abda5 | -17.7162 | -54.18422 | 2026-08-10 05:31:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d028859c-a8f4-354d-abf5-5fb08d53790a | -16.49414 | -54.64869 | 2026-08-10 05:31:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01e95624-3e90-3fdb-84c6-2b57ce5cb35f | -20.78687 | -57.69148 | 2026-08-10 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9112fd1c-662e-3e82-b73b-2c205de80b46 | -17.71556 | -54.1894 | 2026-08-10 05:31:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 967188cb-2b64-367c-a7b9-70a4c9c4d5fb | -16.49709 | -54.65237 | 2026-08-10 05:31:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb916ac-c003-3dc1-aa18-70eabc3667e5 | -20.78617 | -57.69675 | 2026-08-10 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fdf13f3c-f86f-369e-a178-e42a695b8aa4 | -8.9039 | -60.5769 | 2026-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5d00d42c-8d7f-3ea0-9474-01787e29e5e3 | -3.72716 | -59.3678 | 2026-08-10 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff978d48-a6bf-37ea-88e9-72f3e9a03f23 | -4.39818 | -54.78982 | 2026-08-10 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2617d371-1e4e-3291-be18-8094dbf8d81d | 1.10152 | -60.51267 | 2026-08-10 05:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fd2b4dc-ef31-326b-95cc-d487762a3beb | -1.65299 | -54.46206 | 2026-08-10 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87148113-1e64-34fc-bc91-7690e41ebe3c | -3.92987 | -59.13665 | 2026-08-10 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a888527-8411-3417-b77f-6fa4ae31498e | -5.03434 | -56.123 | 2026-08-10 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59ad57e4-7e24-3605-8ee9-c64c60836a46 | -3.93227 | -59.12082 | 2026-08-10 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91b27461-6ce7-342f-9560-5437cf4d7a9f | -3.72542 | -59.36773 | 2026-08-10 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 811bffe6-92ec-31eb-8ed3-dae578324db2 | -2.35921 | -67.21106 | 2026-08-10 05:46:00 | NOAA-20 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70121c67-384b-30d4-a7ed-b41f9aea778b | -5.02849 | -56.12596 | 2026-08-10 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b11491c9-4ce8-363f-8b31-e81631404be5 | -4.86473 | -55.81751 | 2026-08-10 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20cb5b04-4970-3390-bd0f-849c1c53859c | 2.35773 | -60.14417 | 2026-08-10 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f39468d-f74c-312e-8f3d-d5af22a79b16 | -5.02897 | -56.12265 | 2026-08-10 05:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2810260e-53b8-3a7e-b698-62e71a034767 | -1.64734 | -54.46126 | 2026-08-10 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 952394b0-0417-3a2c-b2b6-ab0ce670c31f | -4.39874 | -54.7858 | 2026-08-10 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
