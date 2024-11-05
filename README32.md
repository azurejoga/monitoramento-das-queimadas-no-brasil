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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796b06a1-f8a4-351f-8205-1cf44a779687 | -10.0971 | -68.35966 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 517cefa8-9f44-3f08-ae0e-08f0c9a8c7bc | -7.82583 | -72.79314 | 2024-11-05 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a72f3e8d-c653-3d03-9cbf-5663463007b5 | -9.54062 | -68.52264 | 2024-11-05 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6504f266-3c9e-3036-a38e-beb91276a897 | -10.09047 | -68.3586 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6b577b1-caee-363a-a5e0-6bbab6d7c102 | -9.59942 | -65.69617 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4ec5c8d-08ac-34cc-a3b3-3145a4cfc9cd | -9.51301 | -65.59467 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9d5f935-baa0-3708-a159-408d0e0250f3 | -9.56054 | -66.64716 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43c71f1c-2854-31e5-a1f4-09b2337df930 | -9.50586 | -66.56236 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16b82cb8-dc2c-3465-8d82-e0ce869079e6 | -10.56353 | -67.85871 | 2024-11-05 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cca8135-7474-3bee-a228-03349cf90525 | -10.05502 | -68.54032 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc706f1-8c40-3fab-a196-3a8efd620acf | -9.91045 | -64.79355 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50059fd6-9e47-3dc3-9bf9-650f78ef12b5 | -10.5342 | -67.78609 | 2024-11-05 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4993828b-d800-30cb-b68e-fbbe7369a6d2 | -9.51644 | -65.59521 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64239ab5-f6a1-3148-b817-30ea15924d13 | -9.20293 | -71.92488 | 2024-11-05 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0f3b327-c600-3f76-a3ee-f03b83743583 | -10.09268 | -68.36614 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0da4a6f8-e639-3674-8097-b87d37872e11 | -9.56388 | -66.64768 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78e99d83-4a28-3b76-be50-3f5ea3052d46 | -9.20677 | -71.92552 | 2024-11-05 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca94bd34-03ac-36df-8264-f001f811dcaa | -9.77405 | -65.00998 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1634b5be-933e-39a6-9eb9-1de290b967de | -9.70255 | -64.68114 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 467e1ead-2cba-3577-95b1-5cce42de21c4 | -9.65294 | -66.97586 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9baea784-75b6-34bb-97e6-0f1acc4c7c52 | -10.09378 | -68.35913 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e232e6-a040-3a09-99cf-c554e0f6c417 | -9.53674 | -68.52564 | 2024-11-05 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 016359a2-f867-3eb3-ac47-5df5d1c002de | -10.09323 | -68.36263 | 2024-11-05 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8464575d-69a0-38c6-a515-35c3d114887c | -9.44887 | -66.64443 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a61137ba-8cf3-3b43-ac53-0b76c3ad15d0 | -10.54411 | -67.78767 | 2024-11-05 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 320f0cc1-f761-3893-8e5f-a3173612b5a8 | -10.36416 | -67.98016 | 2024-11-05 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d3e199d-31a1-3fa6-926f-67885ba21206 | -9.01547 | -67.2728 | 2024-11-05 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0b9b208-23b9-3601-afe4-6cd4d5ceab8d | -9.58067 | -65.98212 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1021b5b9-9cf4-382d-9ba4-0cef052a15b8 | -9.56536 | -66.2188 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b8a74c7-dbf4-3250-9f66-938a334728c4 | -9.20548 | -71.92357 | 2024-11-05 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 081076d6-5c2c-30f2-8c04-06b6881110b6 | -10.56683 | -67.85924 | 2024-11-05 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3f8c26ef-34e0-329c-bd83-67e2d95aa555 | -9.97038 | -66.85592 | 2024-11-05 05:50:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 816aa49a-5ac5-3d45-80ad-1a76d7efc7a4 | -9.64871 | -65.74146 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d44402c1-b1c3-3d6b-b876-a982fcf03c06 | -9.596 | -65.69566 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 131a32e8-ab52-3492-8d03-df8ebb2ac7bf | -8.83257 | -71.2513 | 2024-11-05 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f96f5873-0250-300a-a80c-2507e5ee70c1 | -9.77816 | -65.00653 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 077a8446-2cfd-3217-af8e-e68e3fe88a92 | -9.69897 | -64.68059 | 2024-11-05 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db8a2b22-1f33-3d63-8cd4-f8ec64d1d2b5 | -9.47961 | -66.53275 | 2024-11-05 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 100801e2-81fb-3c5e-bbfe-c19ce979e1ba | -10.48285 | -68.65347 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e665591-266d-3382-908b-37976228932e | -10.83842 | -68.40467 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af75dc1d-6b55-30a5-8b1e-7e0b9823cffb | -10.73241 | -69.34689 | 2024-11-05 05:52:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef35f447-0bf0-374f-b96b-ab528e69765a | -10.91616 | -69.20241 | 2024-11-05 05:52:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d15373e5-0213-39bb-a499-f4c5aeeca109 | -11.88766 | -64.0238 | 2024-11-05 05:52:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d9c5b44-09b9-3d51-ad4b-9f6c3c2e721a | -10.51725 | -68.77874 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 404d6df0-0f56-3aef-9148-642d8ec6bfc5 | -11.99241 | -63.52838 | 2024-11-05 05:52:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faee3ac8-7d44-3acf-98f8-6b971daadee9 | -10.91443 | -69.21323 | 2024-11-05 05:52:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a70e8eb9-1c8e-3ee6-83c8-193130f8e29e | -10.74791 | -69.37928 | 2024-11-05 05:52:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50046d6c-d30a-3067-b297-a39165b0eda5 | -10.84995 | -68.26649 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 448923e1-2755-394b-bd79-538d3557b337 | -11.19567 | -64.90256 | 2024-11-05 05:52:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf2675d2-14a0-33a4-b876-6ff1c8dcfba2 | -10.51668 | -68.78229 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a257b7e8-7b6c-37bd-94f4-8c1042f900d1 | -10.71409 | -68.58941 | 2024-11-05 05:52:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 292fa3c3-d211-32b9-97e9-a228d870b873 | -10.87212 | -69.284 | 2024-11-05 05:52:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2ddcbbf-7d61-36e4-a263-97e458184216 | -10.85271 | -68.27052 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 902ceab3-780e-3948-a31c-2f3d9842bf05 | -13.44225 | -61.3875 | 2024-11-05 05:52:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61005a19-efca-3684-854e-9b261cba83b2 | -10.82171 | -69.76849 | 2024-11-05 05:52:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37487da5-1fe5-397b-9e02-cfaddb42d49d | -11.7992 | -64.98601 | 2024-11-05 05:52:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c2ca332-cd28-35e2-b6df-00382c25bdef | -10.85326 | -68.26702 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 946ef6a3-59d6-3d7b-b011-6970ad08cd87 | -10.82463 | -68.3414 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 259e231a-9e19-3789-aaee-72614a6d55a5 | -10.8505 | -68.26299 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17895966-30f7-38e6-a517-fad2dc6cc089 | -10.88183 | -68.41151 | 2024-11-05 05:52:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93e2c84c-5779-3bc6-aecb-0e67703a7600 | -10.83787 | -68.40818 | 2024-11-05 05:52:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecab5a3e-2c25-3c63-b2e3-fcd51e4ec22a | -10.87243 | -69.32492 | 2024-11-05 05:52:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d351ea1-58a4-35e4-9ed2-1c902bc15b6c | -12.28211 | -63.71984 | 2024-11-05 05:52:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df69912e-4499-3185-8a48-1604fa980ea3 | -10.86969 | -68.42396 | 2024-11-05 05:52:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41c36ead-4d93-38e2-b640-2a6dbb63f7e7 | -3.5631 | -47.3847 | 2024-11-05 06:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 73c9bda7-2889-3907-b7e6-4ced77f9a297 | -4.3351 | -48.6292 | 2024-11-05 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| fdd0169c-9c37-332d-a62e-baee86c51ab0 | -2.1876 | -48.8531 | 2024-11-05 06:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 4e233cb9-84ee-3bd1-90c8-2cdd7957dbe4 | -2.6507 | -48.5629 | 2024-11-05 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 49ea7f2b-1835-3e10-a15f-44800c594bfe | -3.5446 | -47.3855 | 2024-11-05 06:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 3a1e1167-d9d9-3a48-977b-af1a64a9d157 | -4.3536 | -48.6283 | 2024-11-05 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0edfa9e3-5b01-3c4a-bf11-1043398295eb | -2.8065 | -51.4855 | 2024-11-05 06:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bb4f3da7-0892-3991-bdad-c53342d36c4f | -3.4934 | -50.3819 | 2024-11-05 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4ed7c0b6-4604-34d4-a956-cb6def41c046 | 3.51371 | -51.25389 | 2024-11-05 06:09:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 26b6f83d-84dd-3068-ae55-7bd2703fd152 | -3.49089 | -50.37841 | 2024-11-05 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0632ede2-ff30-334e-be4a-7eebcfcbba22 | -3.03153 | -53.26974 | 2024-11-05 06:09:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6d6d7d91-362c-31fd-bc4a-39ca8064837f | -2.65609 | -48.54379 | 2024-11-05 06:09:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 83ca7c67-de31-3e12-a501-40bf09ce0b47 | 3.50224 | -51.25563 | 2024-11-05 06:09:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 5df64c38-8e0f-3f8c-9cbf-36051ff6921c | 3.5113 | -51.23842 | 2024-11-05 06:09:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1593bd9d-dccc-31b2-b658-970eec416af8 | -2.65145 | -48.57636 | 2024-11-05 06:09:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b687a751-44f1-3ec9-a0e6-47fa694b5f4a | -3.03352 | -53.25564 | 2024-11-05 06:09:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 572ba3e0-a3a0-39af-a377-8d3570f37c77 | -4.08764 | -53.75678 | 2024-11-05 06:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6554dfc1-5bdb-3fd4-93e7-0f7d2269178a | -3.04249 | -53.27131 | 2024-11-05 06:09:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 36249509-be5f-33ad-94d4-eab931405fb2 | -3.21512 | -53.09986 | 2024-11-05 06:09:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 6fa0c7b7-234a-3c48-9862-51321e5e099e | -2.81175 | -51.47199 | 2024-11-05 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| fa40394f-123f-3f4e-9197-80f6503ea9c5 | -2.79645 | -51.48233 | 2024-11-05 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 99126aca-fae0-356d-b41c-450d3b4a08e5 | -3.10027 | -50.25049 | 2024-11-05 06:09:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| fbbfa79c-6a11-39de-a687-a78af03fbdff | -2.8091 | -51.48393 | 2024-11-05 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3f75abf5-4d10-324b-9b82-b4c9d1ec0cb1 | -2.84188 | -51.79768 | 2024-11-05 06:09:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 8068bdb8-9600-33b8-9555-b2b33ba3f634 | -3.4769 | -50.37648 | 2024-11-05 06:09:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5c577ffa-4201-387d-8c76-01a459827c2d | -3.02936 | -53.26382 | 2024-11-05 06:09:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e6a7583b-1039-323e-8df8-6e4b2965c267 | -2.80911 | -51.49105 | 2024-11-05 06:09:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 294321c9-008e-36c4-949b-ef50c6c1e433 | 3.508 | -51.2576 | 2024-11-05 06:10:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 972e5bfc-3f32-36f7-8963-3349cf77242c | -2.6507 | -48.5629 | 2024-11-05 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8e72c902-7e53-305a-8c20-3ba946e8b667 | -2.6691 | -48.5624 | 2024-11-05 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 47b5bb7f-5255-38cc-9103-409925bd13f5 | -2.8065 | -51.4855 | 2024-11-05 06:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 121d23d5-a73c-343b-b6dc-256c916041b0 | -2.1876 | -48.8531 | 2024-11-05 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 706c26d7-9af5-3103-9c41-8969d64c7cdf | -3.5446 | -47.3855 | 2024-11-05 06:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| dd0d6a6c-030f-3f12-8d87-da42145ef45c | -3.4934 | -50.3819 | 2024-11-05 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 89650e99-ca4a-3bcf-8633-ed0af6a74d1d | -3.5631 | -47.3847 | 2024-11-05 06:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| fd1434e3-f905-313b-8f83-b031b57fb0d9 | -2.6507 | -48.5629 | 2024-11-05 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |


[Clique aqui para ver as próximas entradas](README33.md)
