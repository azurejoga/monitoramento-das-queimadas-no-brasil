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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60969d74-9f64-3711-b390-aae37e69e8d5 | -12.99165 | -45.22147 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb4f503f-9b2c-3c65-8da3-f4edb6b995d7 | -14.84466 | -48.32115 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96034995-f54c-3e9f-88d5-d5633e9f5a7b | -9.9642 | -60.18242 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a56d0a9-bb67-389f-bed2-3cdfdd5550c2 | -14.65883 | -56.57517 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b1ab691-afa8-3146-be09-be5e0a323e24 | -11.53904 | -51.8574 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 0fb95cc9-b221-3554-ae60-d5686b673241 | -14.66551 | -56.57629 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87a56869-dc23-3795-a3d3-a19db3817f6d | -9.01714 | -65.38871 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 74915887-0a82-3b08-b561-5377b818dd4a | -13.16498 | -46.93425 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feb998b2-bf81-3cae-b0d5-04df937397ca | -12.72606 | -48.12016 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cc89648-2e88-3e7c-8557-c6706df6eb82 | -9.00419 | -65.69764 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 71b81e07-36c2-35de-9899-5513bd926964 | -11.52769 | -50.48104 | 2025-08-24 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e820a4b-608a-362b-833c-b81583ad9cc8 | -9.01946 | -65.70506 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a216393a-02f5-3606-8725-04da4ec4a4be | -12.73563 | -48.13067 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8edcbb5-0b76-3e33-bf9c-117c33b23965 | -18.39728 | -46.8508 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acec6d10-57a5-3626-a2ac-9a1ad0e56804 | -9.45438 | -63.50204 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 646061f7-4ef8-3ffd-b415-ef83c29dd16d | -11.83437 | -55.21101 | 2025-08-24 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95be88b4-6baf-31a9-8b51-d0cde35788ca | -14.8227 | -55.9749 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b82ff692-bf36-3064-ac3c-4699a702c9b3 | -13.41089 | -51.79648 | 2025-08-24 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 213538b3-ff7c-36ce-b1c5-18c37817935d | -11.52695 | -50.48618 | 2025-08-24 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738913ad-c592-35e2-be6c-80bf61881f3d | -16.79096 | -51.3505 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d3a9d604-7d7f-3e57-99af-e50e3d789fda | -12.59052 | -60.3628 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 62a48038-8c42-3397-a514-0c78148b7318 | -15.23098 | -48.21395 | 2025-08-24 05:01:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc73732f-183e-3e63-ae01-227c7c27237a | -14.78975 | -47.93079 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e564250e-26cd-3317-a8ec-e87c9d25436f | -13.49278 | -46.90337 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c68c67d-b497-3715-9105-29591591e9ee | -12.5875 | -60.35674 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba75b49e-fc2a-3ab5-a286-89eaa397d9e0 | -16.40598 | -49.94816 | 2025-08-24 05:01:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1df27a2-bd80-3693-8e2d-32bd23f19bc3 | -17.61049 | -44.30109 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d6021b37-0847-38e3-80d7-07b86ecb2a33 | -14.51758 | -52.04191 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e155075-de8e-3fc4-8fa5-9287c0e1b36e | -13.03922 | -45.2166 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d94799e-fa3e-39cc-9b67-6e1cb86d6f46 | -14.79285 | -59.62864 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5272b217-204d-34ff-a355-4e59a767b2a3 | -16.78591 | -51.35738 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 18aeab87-f6aa-3c4a-8255-746dafc49d3f | -13.45125 | -47.02654 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 948a020f-1d26-30b1-9f8d-7fa1705b57ee | -14.46741 | -52.04386 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3bb6415-4cee-3250-a029-3c0e4a13af7b | -13.47425 | -46.88259 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42fb3f02-35bd-38e1-861f-80817f081840 | -9.0187 | -65.68682 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c2cea2f-ae0a-3730-bb67-1e8d32a4ae26 | -16.49875 | -46.75127 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90dc630-87d3-3346-8ff2-bd044a40e30e | -9.02042 | -65.71011 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34cbd61a-f71d-3020-aa02-0d5f48ce6daa | -9.01786 | -65.69115 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbe014e5-2cef-36a1-9a7c-292cc3a3d996 | -16.79957 | -51.34775 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ccbe587f-2cb3-394d-a87d-a3a010a49639 | -14.37687 | -49.16999 | 2025-08-24 05:01:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03bcccfb-4ade-3390-914c-adcce5a0f8d2 | -9.02551 | -65.71593 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 717bdf05-6f64-3358-946d-740242e69143 | -9.02216 | -65.70108 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db157a5f-c051-3bff-97a3-aa9e1ae88360 | -14.78385 | -55.98309 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d83bf934-84d7-3ccc-b919-f53f413c754b | -9.51389 | -60.55683 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffbb7db6-b958-3223-ac5d-63a48cbd6080 | -9.95883 | -60.18903 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ed8c6a3-a27e-3921-b0b1-68d0ade03157 | -14.79969 | -59.61133 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc777c09-6af7-3f58-a3ef-901074464b45 | -12.72707 | -48.12226 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 288b0cbe-5e6e-39ee-93c4-09cb14fd41b8 | -12.54986 | -45.62246 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f61ece8-aee1-313e-910e-46ec594f687f | -13.05065 | -46.31951 | 2025-08-24 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad0cb7d2-747b-356e-9d24-0666a27f4c48 | -15.33868 | -56.2359 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf4c16b9-cba3-3dc5-bdb3-c549af82e611 | -14.36909 | -51.95133 | 2025-08-24 05:01:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e295ff03-785d-3df8-934e-c033e808e43a | -11.5298 | -51.86931 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c87cb52-98fa-3542-9c8b-f68dd6ad199c | -14.66493 | -56.57988 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0a6092c-6a77-3f7d-9fab-d68d6b2e5383 | -12.51328 | -53.81532 | 2025-08-24 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebe873df-79d0-3be6-93d5-55dc437b60cf | -12.72989 | -48.13802 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bbfb5da0-ace3-3a45-8065-99821306c4c9 | -11.6642 | -51.58555 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6029c871-c4fa-3a0d-b340-dd9089a64a17 | -9.80231 | -61.21252 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b0265ef-ad30-359d-8f12-cf6686101697 | -14.78911 | -47.93612 | 2025-08-24 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdda3331-b4b2-3e5e-9a19-fe6f99e2d5c0 | -9.95064 | -60.18754 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71bd8dfe-e568-3d64-86b0-a3c814b3aa60 | -17.59876 | -46.10464 | 2025-08-24 05:01:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9925a5b-ffc4-3be8-a4cb-6892a2239a34 | -14.29132 | -60.37262 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ba04804-ad13-3412-a2d5-2812c29d1ec1 | -9.33236 | -63.19302 | 2025-08-24 05:01:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f6c007f6-304b-3403-810c-45352e704035 | -10.10578 | -57.77049 | 2025-08-24 05:01:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f00ec59-5f9a-3910-87c1-c0672790f2a1 | -11.60369 | -46.23607 | 2025-08-24 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fd423cd-2fa7-3f00-9156-10a32e4dab94 | -13.48301 | -47.02338 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6b04be9-8c16-37ce-87c2-cff2429881ae | -14.29524 | -60.37305 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fdc5145-11d2-3e63-b3c9-42f1d7b5949c | -11.177 | -55.02923 | 2025-08-24 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4abd298-17ef-3674-90df-806149fee39b | -13.0445 | -45.2214 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 170fe160-c0e4-3eda-8ca0-11e06b2c671b | -9.01183 | -65.7224 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c464f3f5-375e-31c4-8072-81257f554c1b | -14.30164 | -58.49776 | 2025-08-24 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aae2c232-0329-339f-9893-77cfb732205d | -9.52373 | -60.52605 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab88f2a-bdd7-39ac-8722-e55eedc831ad | -16.79928 | -51.35449 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 314b9990-990a-30a1-93ad-151dba8392ef | -9.51569 | -60.52461 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1091def6-1483-32a0-9a85-2825ab7c9ca8 | -17.38423 | -44.27369 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cce23b0b-4f0a-3d14-a599-d6511a804187 | -13.47842 | -47.0183 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f46d117-f33c-33c9-9f04-30adac3f5b78 | -13.47802 | -47.02149 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97edec93-3955-3ef8-9ae0-453d1933769c | -11.42914 | -55.0121 | 2025-08-24 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2add8d07-babf-3b0f-8768-d1ce690894ed | -9.02811 | -65.7024 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c651689c-857f-39bf-a98c-3bc2b8d604fc | -13.04402 | -45.22545 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7a57e25-a7f4-33a7-b5d2-993b81effa99 | -11.7031 | -60.18984 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7ab5f15-4be6-3b93-83ca-0c8e9969ea4f | -15.06637 | -48.52826 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5587fd80-065c-3e7d-bec4-d734a812f64c | -9.01431 | -65.69942 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e4acd26c-72f2-3e2b-89cd-4c32f94ec3f7 | -14.77791 | -55.91246 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffb86eaa-f011-30e5-bcf2-0dffa29df826 | -11.54667 | -51.90701 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26ce4500-5de0-3912-ba08-c579e756b9bd | -9.63095 | -63.09942 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6920449c-a4e6-36da-a88d-1edae1a7e40c | -9.7979 | -61.21176 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f10f33-1dd9-3804-8e94-d016695c07a3 | -12.95103 | -46.28719 | 2025-08-24 05:01:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc75ba43-cb0e-38cc-be72-84d3c82089f9 | -9.51812 | -60.55756 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c450894d-77e6-3ddc-b2e5-6b2f28e7cdce | -9.01012 | -65.72198 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 123f6b86-c731-3a79-958f-32b0393e8def | -11.53444 | -51.91394 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4260ecb6-026d-3d88-8f48-3388838a8113 | -10.41634 | -64.41805 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| daf6f07b-461a-3639-81e1-cd6642e365d0 | -9.01782 | -65.72359 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b1dbc90-b9d7-39ec-bb0e-328d78e6e0e5 | -14.76787 | -59.65416 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86f4ec4a-3681-38d0-982b-65f7b9fed103 | -13.0397 | -45.21253 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd8a6a7-7e5c-32d7-a821-4aa3d60e1ee6 | -9.81689 | -64.26538 | 2025-08-24 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f22a5d-6a41-3829-a2e3-7b764382b84d | -14.82327 | -55.97133 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 182ecbd9-fc1a-351a-aae7-adebf2f3e069 | -18.39872 | -46.84453 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d391c57e-225a-3df4-8789-f82413614b9b | -11.69911 | -60.18912 | 2025-08-24 05:01:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4586ba18-b9e4-3a37-8f31-2e53b01ab82a | -11.59841 | -46.2353 | 2025-08-24 05:01:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f734ec0a-2d64-36bb-8abc-e0142d2d3d9a | -13.03874 | -45.22066 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README68.md)
