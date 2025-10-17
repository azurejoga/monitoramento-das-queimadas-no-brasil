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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef62aa97-ce25-31b9-878c-e51002ab9573 | 1.77552 | -55.73883 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 843cfe6f-728b-3c18-aed0-905775d69e30 | 1.72311 | -55.79962 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23dacfd8-b2a1-355f-8eca-89aa9939ee2a | -0.89879 | -47.54392 | 2025-10-17 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 632cf7e7-42a6-36a4-996e-9cf08646655e | -0.90227 | -47.54447 | 2025-10-17 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c84b7529-01d4-3e7f-bb56-0ac9de05764b | 1.8003 | -55.93256 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 609fda05-7db8-341a-8173-5960edabf11e | 0.33178 | -51.35751 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5737c5d4-bf04-3a2c-8489-dbafc451e54e | 1.85604 | -55.66771 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e3a01b7-d0d8-3293-8d27-aa4fb590b5bc | 1.83408 | -55.70253 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6255d6f4-b103-3ca2-96a2-0bcb3cba2b89 | 1.82513 | -55.70387 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3551b04-180f-3db7-9aa6-5624c4e6e563 | 1.85778 | -55.66419 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b14b8c7-415b-33bd-a599-97b1be11071b | 1.81204 | -55.73769 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6ad040c-10af-3ccc-9106-574dfab49ca8 | 1.8492 | -55.6823 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 175062c9-1ff7-33c6-b339-f0c2d5a44f91 | 0.33805 | -51.35275 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff5ae598-b8a4-3aa0-8584-9bc97e560ab3 | 1.74655 | -55.77304 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99b5f3ba-050b-3124-851c-6938f5d0b0fb | 1.85674 | -55.67211 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b9fcc5f-8c87-3d6e-8db7-cc535341ebc5 | 0.9685 | -51.60461 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e047855d-1af5-361a-8016-12fb8a5a0b1b | 1.0484 | -51.20724 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a37c61f3-ccfe-35d8-b106-8f3d963862f2 | 1.82272 | -55.7178 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 86cb803d-2680-3833-9d73-81c6b38f7157 | 1.87521 | -55.84699 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6515c7d-ad3d-3967-bcad-4324e5f82282 | 1.78001 | -55.73814 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 864c7180-5f3e-38ea-b9c6-3b713558cefc | 1.76789 | -55.74899 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f0021f6-4a2d-3fe1-a670-5117a526afef | 0.34148 | -51.35221 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b25910-7773-3256-ac94-d23b671c2cda | 1.8296 | -55.70319 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 60a998e4-4449-3fce-a951-ecea925b81d3 | 1.77171 | -55.74394 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b2d2158-4b9e-3180-b11a-fcbf73ef31d3 | 1.84543 | -55.68737 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28392be4-dc0e-3fd6-875e-62d680e94342 | 1.7307 | -55.78929 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf263119-ffb5-33e6-9d68-179054c23892 | 1.82203 | -55.71336 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 565920f3-41d1-3857-acd6-f2fcd0929d33 | 1.98774 | -55.93613 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f4b3f9-b5c6-3f04-9097-e4c2ac8762b6 | 1.7513 | -55.76065 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56898f38-2fe3-3667-9c74-9e50d79858dd | 0.87506 | -51.12444 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34f8e327-2f54-3460-8ff5-d92600ff2287 | 1.78585 | -55.9048 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d60879-5023-3b9b-9b18-bdca5e86d951 | 1.78189 | -55.90288 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7feb0578-d462-3648-bf5d-08e621e31d57 | 1.03811 | -51.09621 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ce9dedf-cea9-3d90-b41d-e855fc20bc59 | 0.87165 | -51.12498 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dafc669-cf9d-3043-a229-a477a7f304b1 | 1.04525 | -51.20728 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f746f3ec-2891-3608-b3df-3f907685ded5 | 1.09909 | -51.15039 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edaf94d6-d7aa-3cff-8e6d-acaa8feee482 | 0.33236 | -51.36119 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfad4832-a1aa-3565-b8bd-57108980f720 | 1.04436 | -51.09149 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85faf820-7a05-3a6a-82e5-95be57d52d98 | 1.73139 | -55.79372 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48047c76-455b-34c5-83e2-144df48ebe66 | 1.79591 | -55.87303 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7a6f420-bad0-3d2c-87f0-8eaa80dc2945 | 1.81962 | -55.72736 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1bba483-f2b6-3d7a-969b-e3edde4a72ec | 1.04183 | -51.2078 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e53986-7fb1-348f-9625-a5165e860874 | -0.87932 | -48.08432 | 2025-10-17 04:46:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b5e377-703f-3bb0-bd83-8c4495eeede5 | 0.32836 | -51.35805 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9df0a153-3be5-3bfa-b47a-957b61209dcb | 1.01315 | -51.15961 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1049792b-1423-3ea8-9f9e-b16737f1c5c7 | 1.73898 | -55.78339 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bc186c02-cb5c-3cd5-915d-bf1544a89002 | 1.84323 | -55.68904 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af95ddb5-4325-3046-be27-68c91671c675 | 2.05583 | -55.7444 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f88d4eb5-8d16-3a0e-8eb4-9d1557ff5cdf | 1.78347 | -55.9191 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc5bb54b-51f2-316f-b578-c236acc423c8 | 1.82651 | -55.71272 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d1cd95a3-b2d1-3965-8b70-3932ec6cab5f | 1.7842 | -55.92368 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6d253fa-f3c2-37c7-abe9-5450d0f51400 | 1.0347 | -51.09675 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da7587b7-2d77-3503-bcaa-f2f31e26b94b | 1.78643 | -55.90222 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce266725-c4d5-3c55-a262-a89d00ce1f08 | 1.39059 | -50.85248 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d12a6e2-29e0-323f-843e-29a8516d8361 | 1.85845 | -55.66861 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35fe029f-4b30-3bad-b0fe-00e5900facda | 0.69062 | -51.46228 | 2025-10-17 04:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a395131f-be88-3e63-ae36-4c7d3c59072f | 1.10251 | -51.14986 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb01dfd-dd77-39e9-a1da-bcc5cf306913 | 1.02901 | -51.10514 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65ebc3b9-73b4-3496-b0bb-3efd222a5b65 | 1.79342 | -55.8871 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7dcddf-ca39-3ae2-b481-89c3c3da687c | 1.85399 | -55.66931 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddfab789-a5b8-34ed-bc6e-00fc3f58d72f | 1.78118 | -55.89812 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22b85583-e810-38d7-bf50-13944db0c361 | 1.81584 | -55.73256 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b1f2591-28a7-3760-91c9-872884d3bf96 | 1.04498 | -51.20778 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ce302e1-6f17-33ac-a7cd-1ef921e35ec2 | 1.04095 | -51.09202 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a7e6b7e-a966-3dfb-92bb-accf1fb2e1e4 | 1.83029 | -55.70761 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31ba1caa-0104-3f26-9f72-a83b4f8932af | 1.85228 | -55.67281 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb97d669-09f5-3aa1-bfa9-a2682fb6815b | 1.84474 | -55.683 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e104dac9-80bd-3d1c-8145-c8e81d213819 | 0.32894 | -51.36174 | 2025-10-17 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cb88372-b710-3568-933a-967fd1ccbd84 | 1.04555 | -51.21146 | 2025-10-17 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 659d84ff-a087-34d2-9339-b666584c4688 | 1.01998 | -51.15855 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae2f1ca8-9f0a-3307-b978-9bb22f648bdd | 1.74682 | -55.76139 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdd5461c-1477-3703-bef4-7df14f25c1ff | 1.78918 | -55.92048 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 049c4ba6-5c63-3e92-b679-4055d194693c | 1.83339 | -55.69817 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5d5d1daf-f892-3d01-8bff-a8b5a79dbef3 | -0.89818 | -47.54774 | 2025-10-17 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5137ed8-90ef-390d-9d46-a12d2aaf5d6b | 1.82892 | -55.69884 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f80f8ebb-11b4-3de2-8a73-d281405add21 | 1.74814 | -55.77025 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aeee7bbd-4900-30e1-8b84-6e2033db994f | 1.86224 | -55.66348 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8264de89-e86d-395f-b27e-2817f01bf6a5 | 1.78572 | -55.89753 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3beb3d2-35b1-32d1-9c87-c229909cbea8 | 1.73588 | -55.793 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f66cb9-a691-3521-a552-550708c76367 | 1.84704 | -55.68395 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1490d38-3ead-3854-ba12-ad439b050f84 | 1.801 | -55.93714 | 2025-10-17 04:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08675e3f-129e-3e48-b5fc-ab1779bfd9b9 | 1.01657 | -51.15908 | 2025-10-17 04:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| db04c265-201e-3351-adf7-821ece214fd3 | 1.85911 | -55.67303 | 2025-10-17 04:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce006e6-4242-352b-895c-0ff24492d9d3 | -6.82318 | -41.69117 | 2025-10-17 04:49:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0b14ffa-0a78-36bd-a9ca-84cc13c0c8e5 | -6.23911 | -41.54276 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ebe74871-bbe2-34c7-90e4-f0e255f59e68 | -5.3341 | -42.90411 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aa066166-1632-31d6-b681-22d4650d07db | -3.49064 | -50.08949 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9356df0-56f7-32ec-a364-853ecdde9c9b | -5.86853 | -44.83701 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaa57ca2-c401-3da6-87a9-a580fe0c915c | -6.03099 | -41.90706 | 2025-10-17 04:49:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4dd7b5b7-a82c-3213-bf9e-0ddce8edeef1 | -6.31929 | -40.94936 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c2ce3e36-844b-31bb-91a3-9e47da726e55 | -2.8641 | -50.73477 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81657bdb-c07e-30f8-988d-7790a388d2d9 | -6.69487 | -40.87142 | 2025-10-17 04:49:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 448248c2-a3b1-31e3-bb99-2090b46992c4 | -2.74191 | -49.38781 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d214db68-74a3-3922-83e6-f5f6da65f030 | -7.11234 | -44.73905 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70fd9ea1-76f6-3fdd-a7a2-938e76cbb4a1 | -7.83442 | -44.14266 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1ab3535-5241-3866-a6d0-5bb16a718dd1 | -4.81028 | -45.73069 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21afd358-e1d4-3991-aa8c-e078d407c37e | -6.99468 | -39.23305 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3b0c6096-fc37-3e61-9f2c-c14455776395 | -7.33062 | -44.15269 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 973c28c9-bc91-3a6f-bd0f-6e3a38e978ce | -4.26075 | -49.69169 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cef0e4b-586d-34cf-9d49-e5c058d4e189 | -2.17311 | -48.4238 | 2025-10-17 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README75.md)
