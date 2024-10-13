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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc0ed2ab-56e4-330e-9bcb-640c9a91bc02 | -6.13755 | -44.73065 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57936706-cfaa-3c43-a0ad-eccdd9b93b48 | -6.13516 | -44.63767 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b531c3a1-9a37-3132-9120-f96c8f53cb25 | -6.13436 | -44.72507 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7cb0b70-3399-358d-9142-7be9f12a4224 | -6.13196 | -44.63198 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a90018e1-4b25-33b2-aab9-a35a36803a6a | -6.13122 | -44.63708 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8c5ac3a-b1fc-30bb-8f08-21fdfb83f774 | -6.09259 | -44.84595 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cad0448e-82ee-3277-b72c-c59ed6c00924 | -6.08942 | -44.84044 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 357fa8d4-0610-370a-9f88-f3a47ddb940b | -6.08869 | -44.8454 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 678496c8-5a09-32f4-944c-a4399a187628 | -6.08552 | -44.83986 | 2024-10-13 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdfd28fe-e520-3b54-9857-3dd90f715dad | -6.07677 | -44.62675 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9bc05faf-a18b-30a0-8028-e15d3c0ee0b7 | -6.07601 | -44.63176 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfe02db0-ee53-3635-b1bf-9ac38b257a0b | -6.07207 | -44.6312 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcf6a083-b8fc-3d46-8b78-9c2e12c78d2d | -6.07131 | -44.6362 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65baf43f-bfe7-3039-97a3-4697969f9682 | -6.07068 | -44.05619 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98d827d9-dcf2-3b50-9312-2d937eaff9ad | -6.07015 | -44.05521 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3da0dfb-306f-3f7f-ae5d-98d7a18d469d | -6.06963 | -44.05883 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69163ca3-e981-39fd-8e6f-ac3590be880d | -6.06737 | -44.63564 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2599dd9c-d226-3454-b161-9d102b10dd99 | -6.06662 | -44.64062 | 2024-10-13 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0e488b3-661b-30b1-ac4d-353c6400bb71 | -6.06661 | -44.05545 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10d4565c-10a6-307f-abb3-96b204c3bdb5 | -6.06607 | -44.05448 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ac6fd9d-87ee-307a-a283-8ba0ecd15378 | -6.06556 | -44.05805 | 2024-10-13 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23a6152e-cc05-34d8-a4bd-d2d457eddabb | -5.89036 | -44.31506 | 2024-10-13 04:40:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c86ffb7-4218-3f39-8043-575c43b6bc6d | -5.88983 | -44.31861 | 2024-10-13 04:40:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d90919fa-a2a3-32f4-b7d3-0eb6c9cbb1ea | -5.57031 | -44.22746 | 2024-10-13 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb2e66ad-1473-3781-8984-8ba82d3e3c83 | -5.473 | -44.26277 | 2024-10-13 04:40:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b0246c2-a11d-32a1-8c3b-e3ceb1099a44 | -5.42831 | -44.28812 | 2024-10-13 04:40:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24bd9d85-9be2-3c04-b7bb-113bfaf5cce6 | -5.4278 | -44.29163 | 2024-10-13 04:40:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99749c57-f484-3dde-af5a-9298af0bc205 | -5.35371 | -44.41689 | 2024-10-13 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 090b671e-5ba2-30f5-afc8-82fc7351cd6c | -5.16776 | -44.36635 | 2024-10-13 04:40:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37d2c7f3-8d6c-3de3-a3f8-526d674e4493 | -7.07232 | -43.84659 | 2024-10-13 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39062243-ef8e-3bbb-af1f-2596c33fd3e6 | -7.07215 | -43.84417 | 2024-10-13 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f7e14bd-53ed-3071-adf4-dfa55caa0c18 | -7.06376 | -43.96847 | 2024-10-13 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e56510b2-7ac9-3c3c-8b76-4420ccf51239 | -7.27813 | -44.96836 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66f6fb01-6bb2-362a-b74e-c3b48a8a1dcc | -7.27742 | -44.97327 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35423a63-71e8-3b52-a875-afefc46ffb5f | -7.27421 | -44.96776 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 625e541e-ada8-3060-aaa7-c0caaf29b6c9 | -7.2735 | -44.97266 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeed48ff-95c8-34b2-a4f4-de310b27db08 | -7.00047 | -44.70013 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26d0fcc0-ebc2-3aaf-af47-d1a9ea4e2497 | -6.92708 | -45.14751 | 2024-10-13 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 92bc85cb-c61b-3292-91d0-05f35e2c6bcc | -6.81798 | -44.46681 | 2024-10-13 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c76d0c7-45b3-317b-8252-148e1bdca119 | -6.81343 | -44.46975 | 2024-10-13 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fe44158-bce5-3ffd-abb7-29d2ae99fd9f | -6.75054 | -44.18584 | 2024-10-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c0d4778-b868-35b0-ba85-d4879111072a | -6.74645 | -44.18516 | 2024-10-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798eb7fd-9a25-334c-9fb6-ed0d2d45fdb6 | -6.68612 | -44.62782 | 2024-10-13 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68434f2b-3233-3f7e-81b2-6ede672e2257 | -6.58527 | -44.17924 | 2024-10-13 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e26699b-5fed-34a9-b6b3-fd6378485278 | -6.58115 | -44.17883 | 2024-10-13 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18c37f09-946e-3899-b385-92b8a73b7d98 | -6.53565 | -44.42897 | 2024-10-13 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2e81a89e-0a9d-33c1-b921-a2f818914b0f | -10.92802 | -44.65826 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f66a8fcc-602e-3493-b4d2-7e37733aa31f | -10.92435 | -44.65368 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa85249-216c-3bc6-b20d-ca30004c5320 | -10.71454 | -45.05184 | 2024-10-13 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaaefc37-aadb-3f9d-8f5c-ebd18c47cfdd | -10.71402 | -44.48802 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fe06562c-8dc1-329e-9be9-71a230e2554b | -10.71344 | -44.4922 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aa0d1787-9315-38b2-a08d-ee241abd2bab | -10.44725 | -44.94567 | 2024-10-13 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 267c7b2e-821e-34ff-8a72-637765316f2f | -10.44672 | -44.94941 | 2024-10-13 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bd5aa46-f637-3a6b-be6b-89e15a8da3d9 | -10.03692 | -45.02487 | 2024-10-13 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad614f84-3c36-344a-8fd8-418ddcb5f504 | -12.32685 | -45.00401 | 2024-10-13 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ceba441-3bad-3053-94cf-7adcabe4ffab | -11.84363 | -45.12205 | 2024-10-13 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20eaa47e-41c8-39de-9877-340cf8cb30b8 | -11.12994 | -44.95516 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3768b86e-d9ac-3ba1-a9c4-35e7758b11cf | -11.12835 | -44.95215 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f249cbd0-bcfe-3861-8b12-420b8c6742e9 | -11.1278 | -44.95604 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75ad2aaf-72ff-3505-b4c9-d03efc573927 | -11.12579 | -44.95452 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bab9400-0fb1-33c9-88ed-cd5e0e1b1b51 | -10.95634 | -44.64031 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b2a22fa-a823-3d4f-a653-893b8b57d4b8 | -10.95211 | -44.63971 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e6a23e4-c697-3181-8d01-77e3735baf3d | -10.9484 | -44.66761 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88191810-f3bc-3ed5-93bb-58af4200840d | -10.94803 | -44.66917 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f446a863-cc01-30ee-9acc-c24fe3981650 | -10.94492 | -44.66062 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 23c808bb-3a9b-300c-9ff1-41d0c894df18 | -10.94436 | -44.6646 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| fd86ae46-752b-3a97-a8e1-b9c3c926b275 | -10.9438 | -44.66858 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| cc7d67a8-1d91-3ea6-8773-b50a3e3fae32 | -10.94325 | -44.67255 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73e92214-7b69-3eec-91a3-39fea6dffe2c | -10.93958 | -44.66799 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d3ae123-04c2-37af-b022-3ae62ae1d6b9 | -10.93902 | -44.67196 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96cd0d57-c226-3b11-a9d5-aca8041ddb29 | -10.93791 | -44.67988 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e97a4df-7fb3-3136-af91-c8b7d39316d5 | -10.93736 | -44.68385 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 323e8461-7ab6-39b5-98eb-76c545c7cc78 | -10.93536 | -44.6674 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 067d1c80-30d5-3ab3-9212-24cc78bdb8cc | -10.9348 | -44.67137 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec9e09ab-a39e-38db-90ff-86c5e498987a | -10.93425 | -44.67534 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca3fc7e9-7c82-3e02-9d35-4a9f4aad6f0a | -10.93369 | -44.6793 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31204b1a-add3-3849-b8d7-2e3f787f3251 | -10.93314 | -44.68327 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 834fdf6b-73f9-3e0d-b612-199f4db5c400 | -10.93003 | -44.67476 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02c3e2e2-d001-3ca9-a464-cdb217735543 | -10.92947 | -44.67872 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3be9dfbe-d60e-312e-abb8-13037d0a5db9 | -10.92892 | -44.68269 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec9ff2a6-fbc8-37ad-bfe7-c984305438a0 | -12.32668 | -45.32119 | 2024-10-13 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff3583b8-219b-39be-ad53-8184e8a15a13 | -4.99464 | -45.47317 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c908527-e02b-375b-8cf1-28d7ed9d9f22 | -4.99369 | -45.47162 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 783103af-d834-3df2-9f32-2925ea35c6c4 | -4.95807 | -45.76202 | 2024-10-13 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c519db42-01a4-3f27-9353-631ffc7c376e | -5.47481 | -45.83633 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21215f42-99ed-3773-8584-455d27334d4a | -5.06754 | -45.38358 | 2024-10-13 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a5f4c74-788b-3ff3-aaba-804c18fdef43 | -5.70485 | -45.6757 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b303aace-3dbf-33ac-ac82-c65043f17d44 | -5.70116 | -45.67518 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 379e7933-6d57-30b2-8e84-5c560dff1935 | -5.6022 | -44.96595 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17c8b263-eebf-3235-8e09-7b0b281629a7 | -5.6 | -44.96395 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18735292-fe04-3a6e-821d-f6bfe6afb457 | -5.49671 | -44.9728 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c591c987-82c9-3707-ad34-6b1c1865a9fe | -5.47544 | -45.83203 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efe00230-dc9f-3973-abdb-1a96062615f5 | -5.47466 | -45.83395 | 2024-10-13 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 508068d1-2b23-3a7a-ba07-62b3f9662571 | -5.40385 | -44.9298 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f863f417-fc68-3360-9acc-af13b37d8bbd | -5.4029 | -44.92727 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5727cb56-400d-347d-9160-83f980d6a200 | -5.39006 | -45.04163 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84fbe950-14d1-335a-8363-503cd98d2860 | -5.32139 | -45.0094 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c655fbd-2586-380d-bcf7-3559c0e3dc4b | -5.31459 | -45.41179 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82af4b8f-cbe0-3479-8dc1-4a1c2cb9fdcf | -5.29944 | -45.23386 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8576e127-e691-3c0c-9926-6807b036a279 | -5.29568 | -45.23324 | 2024-10-13 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README61.md)
