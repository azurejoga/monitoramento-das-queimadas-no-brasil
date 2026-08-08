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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8737538e-d6e0-3994-ae90-685ce874a734 | -18.34639 | -50.72853 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d4df47d-dd96-3330-bbb5-744b4aa1d1a2 | -18.34696 | -50.72474 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bf815d8-89a1-338c-beeb-7c78ef9de7dd | -19.85105 | -43.46742 | 2026-08-08 04:49:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5d6603a3-aa1c-336c-8c87-14be5ae84dbb | -18.36071 | -50.70605 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 090fa8c3-c0ed-3b73-ba28-5b030f8c45be | -19.63828 | -46.19989 | 2026-08-08 04:49:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef5bfed7-ab4f-340a-8ca2-1b887d4f2476 | -18.36637 | -50.69123 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d584c7a-5508-3d2d-908d-d681821a7c3b | -16.68152 | -51.36642 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e246eb58-72ff-34cb-ba4d-3093902f5fa2 | -18.36059 | -50.70351 | 2026-08-08 04:49:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 395ff3c7-ea44-35ec-a395-8125d26ab8ef | -16.68484 | -51.36699 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cd2edf1-5cdc-3ba3-aead-4ffb36c7a977 | -17.88123 | -43.77917 | 2026-08-08 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61a5bc79-4d49-32b2-8dd4-17a335e21901 | -17.88089 | -43.78217 | 2026-08-08 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33372179-ea01-3484-b6d4-9d91249d92a8 | -16.68595 | -51.35976 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf98f929-9c4f-3e97-9ef0-abbe29de20d6 | -17.8809 | -43.78218 | 2026-08-08 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54560eae-b6de-3d29-a579-cf5ef5ce4fe9 | -17.54927 | -49.63071 | 2026-08-08 04:49:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9389253a-82d9-3592-824c-ba1a9c302c6f | -19.78457 | -43.73308 | 2026-08-08 04:49:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 172dcf01-acd4-3f48-99d8-983b1e49331e | -16.68264 | -51.3592 | 2026-08-08 04:49:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e4c6cb2-918f-3886-a71b-029aece8d4a5 | -18.21481 | -44.35756 | 2026-08-08 04:49:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22363d76-a604-3c1c-af6e-de8e836c45b6 | -17.83927 | -44.49298 | 2026-08-08 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 013105c9-cc88-3844-9cf5-27ac41bda646 | -4.2635 | -48.1799 | 2026-08-08 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d644b9a2-e532-3daa-8962-3c0365625831 | -4.2634 | -48.2016 | 2026-08-08 04:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 479b308f-0b89-34c7-8801-5d8d57f672aa | -4.2634 | -48.2016 | 2026-08-08 05:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b3dd7148-56c0-3c40-917b-21b78db8cc63 | -18.3743 | -50.6786 | 2026-08-08 05:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 75393675-d54b-39cf-b949-a1859be7cab9 | -18.3738 | -50.7008 | 2026-08-08 05:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 41c3f0bf-2039-3f9a-aa2f-1969e2477525 | -4.2634 | -48.2016 | 2026-08-08 05:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ba53e326-7608-3b83-bc8b-e0546ecb934b | -4.2634 | -48.2016 | 2026-08-08 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 47b494a4-9a28-3b64-aa34-bac0a669314d | -4.26785 | -48.19559 | 2026-08-08 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4cd894a6-ebb6-301c-a5a0-2772722be988 | 1.76783 | -60.23221 | 2026-08-08 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01ed2ca-7cac-3a67-b812-5f35df5e51f1 | -3.02622 | -54.52714 | 2026-08-08 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e00eaf-7fff-3eb9-ada5-bb224d620fa8 | -4.26881 | -48.18878 | 2026-08-08 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 344bee41-b744-3198-b53b-5e941ad60eb3 | -1.58758 | -50.43797 | 2026-08-08 05:27:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16dd6768-6348-378a-8b4f-9f754a06fb20 | -4.2735 | -48.19101 | 2026-08-08 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f6c4442b-2d83-32f1-9725-8e89acde4c6b | -3.96794 | -48.12412 | 2026-08-08 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cfee8fe7-3634-3249-95de-ab5edd055196 | -3.96615 | -48.12414 | 2026-08-08 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d1f1a73e-5d88-3faf-adc9-2d02d97fb85f | -4.46227 | -47.92449 | 2026-08-08 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 128e4bb3-6f31-3e07-ba45-d25a25c1b949 | -2.79041 | -49.52598 | 2026-08-08 05:27:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fb81ee7-fc04-31e1-9c81-91d7f413d076 | -3.96096 | -48.12277 | 2026-08-08 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 12469e40-1f4c-3d83-bf9e-deb469e826d9 | -4.26083 | -48.19455 | 2026-08-08 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff23701a-9a24-3c26-8dd8-61ec5b289f51 | -4.45513 | -47.9234 | 2026-08-08 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5a209cbb-fbbf-3e74-ab1c-d921cae4b898 | 2.04121 | -60.87202 | 2026-08-08 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1995593c-ea48-3b05-9ce5-dff453e32332 | -1.58694 | -50.44222 | 2026-08-08 05:27:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47a8ebc4-9519-3ae5-8378-9f1d126f1ec3 | -2.94063 | -54.1544 | 2026-08-08 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fbf70fc-fcaa-3feb-bd1f-ea7fc576a1b3 | -3.95401 | -48.12119 | 2026-08-08 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3faa3ed-4be5-3bc9-88dc-df33b70423ae | -7.55156 | -61.16176 | 2026-08-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f13b0fd1-4774-3791-8d0f-c39df031dc32 | -6.73333 | -58.58366 | 2026-08-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 650637be-b4dd-361b-8786-3f4aa6393234 | -6.70805 | -58.95562 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eee3a2e1-fe7c-389c-8103-eff235993329 | -3.38673 | -59.4562 | 2026-08-08 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6c9046-25be-3cd9-aecf-8eca18d38707 | -3.39592 | -59.44234 | 2026-08-08 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3cb1fd1-0a8b-3522-88f0-a453adb2084c | -6.41668 | -55.78815 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23e5681c-b82f-3809-980a-8ef985554656 | -4.00459 | -56.23534 | 2026-08-08 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ead8ee5-cd00-3fd7-8e6f-f8b6f4581d34 | -4.00259 | -56.23222 | 2026-08-08 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab0b574f-b11e-3c80-8b39-a2306d4d9a70 | -9.09173 | -59.48082 | 2026-08-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f03d9983-50e2-31a9-ae1b-9e0def7300da | -6.71105 | -58.96038 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa28f506-9ea3-3169-8ad2-e5f37de62802 | -6.88746 | -59.90348 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa68d14a-5db9-3e5f-8098-2ab13bd45535 | -7.55101 | -61.16533 | 2026-08-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe38a012-19d7-32cc-8c4c-cd8d0b8de05f | -6.60489 | -56.36459 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a9ea664-c0c1-39bc-8d92-497e18de337a | -3.84183 | -59.30315 | 2026-08-08 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 455c4e1d-3dad-31b0-bb21-ea57cc6962a8 | -6.64856 | -56.42336 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaf00871-9e5b-37e3-b67d-0a0a5b87a824 | -6.28324 | -64.14941 | 2026-08-08 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cde8228-c6eb-346a-9fb5-b1fb171d2da7 | -6.88805 | -59.89964 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0e75bab-2df2-39c6-a172-241faf3739cc | -6.88863 | -59.89579 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47477252-251f-3221-8092-37cff7a7e381 | -6.28607 | -64.15368 | 2026-08-08 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c8981b36-a23b-3eb3-b04a-c4b63728023d | -7.55265 | -61.15462 | 2026-08-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33f2c6c1-5630-3bd4-a24f-ee128dddbd99 | -6.60919 | -56.3649 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a8d8b5e-052c-341d-bcad-923906a93a28 | -6.28667 | -64.14995 | 2026-08-08 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ff3a1777-bbcd-3534-9c90-d2086a4a7fb9 | -3.3833 | -59.45568 | 2026-08-08 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e03d180f-e833-32c2-8150-f6ae49d9d187 | -4.00046 | -56.23471 | 2026-08-08 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fe8cb84-fb4f-39ab-8bdb-f2bed2002ecf | -8.68513 | -62.8669 | 2026-08-08 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84da788-d390-3daa-bdd7-3e2ce0330b0f | -6.84436 | -58.97311 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d659971-b8ba-31dc-93b3-c92d80b101fd | -6.84861 | -58.96943 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1d23930-b057-3fb2-a7f7-bd5670733f16 | -6.73267 | -58.58813 | 2026-08-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 513bd484-2a1e-3158-aeb6-5a576a153cf2 | -3.11659 | -59.92876 | 2026-08-08 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17d5b3dd-6920-3422-aef5-086f9db80863 | -6.88573 | -59.89138 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604a2807-915b-3916-89e1-ea14576abfe2 | -8.16464 | -55.42375 | 2026-08-08 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27f9485d-bc6e-37fd-abc4-f05bf39f8354 | -6.54819 | -55.29829 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eda92b9-1ab6-3d3f-8e69-c0c9a522cd2d | -6.84497 | -58.96888 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d3050a6-4c5a-3f11-8c5e-25c361406795 | -4.70055 | -50.44147 | 2026-08-08 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bb38723-3842-3ab8-a192-75d90dd5a64d | -3.83836 | -59.30262 | 2026-08-08 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e47a6bc4-c379-32cc-8270-8fb409e00322 | -6.8927 | -59.89247 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e2fd4f6-46f9-3d97-ac68-ccb15fb08855 | -6.84374 | -58.97735 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4bd1aba-e851-3ed7-a1f0-c7fa11bc5d46 | -6.83923 | -58.97844 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73282fad-58ca-3759-96cd-1196878ae33c | -6.30755 | -52.81205 | 2026-08-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54a6ffd6-b05d-3a98-bc2a-aaff4fe883b0 | -7.03758 | -56.51147 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5908f410-94db-3e8f-a798-9d0a8b440801 | -8.15071 | -55.42159 | 2026-08-08 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d6ad16a-8386-391a-be8d-8cec0be3d00a | -7.56216 | -57.688 | 2026-08-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c30275a2-ed1a-3907-a1a1-e63f1fd12906 | -8.16532 | -55.41883 | 2026-08-08 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2d8df456-5d2d-3f73-a0c5-0f032f6a89af | -7.31803 | -64.70324 | 2026-08-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9199fa41-2439-39a1-8ce6-ad0bef293fce | -6.72278 | -58.93182 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62de70cc-5a66-319a-b9e8-2a5a215be173 | -6.84415 | -58.97054 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e47587e-8de0-38af-ae7b-3e5c602d278b | -5.88299 | -57.654 | 2026-08-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 598db968-2fde-3e80-9b5f-f3923f1f418b | -7.98595 | -62.02694 | 2026-08-08 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ba45943-d972-33de-a84e-c48449c9200c | -6.30707 | -52.81544 | 2026-08-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c65d65-8573-32cd-8151-60a95ee38fba | -5.8835 | -51.72645 | 2026-08-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c5e28ae-71c4-3b7e-a2b5-f19d25d9a52f | -6.60976 | -56.36088 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2019dfe-0c18-3684-9978-39742cbb4e4a | -6.84351 | -58.97477 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2111a193-77b3-367c-b338-7514b883cd0b | -7.84791 | -56.58859 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a9cc25d-e67a-3dbf-82fd-4d8b8f11e92a | -7.85067 | -56.59148 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f562c51-1cb5-368a-b32c-01c9d2f4efe1 | -7.04182 | -56.51212 | 2026-08-08 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed9aa90b-9bf1-31f7-8c33-8b671c3e9ac2 | -3.37986 | -59.45515 | 2026-08-08 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd0f39d-71b2-3fb8-a7ac-cbc3fd777c22 | -6.88921 | -59.89192 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f041628b-226f-3c1c-9267-761cd280e921 | -6.70742 | -58.95986 | 2026-08-08 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
