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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0164aa16-c2b5-3ee6-9eae-e3adcbc676c9 | -21.44762 | -43.78376 | 2026-08-07 04:12:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d477d920-ca20-3622-9b25-3015e135af2b | -18.92812 | -51.38784 | 2026-08-07 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 979df5f0-8a0c-347c-8d85-0b6176b3148c | -22.93024 | -43.28446 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7aae834a-6aa5-3fc9-a23e-0fb413fbabe4 | -23.55027 | -47.18038 | 2026-08-07 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6d9f9579-0ca1-3a34-b380-6222c7fbd2f1 | -19.71047 | -48.13656 | 2026-08-07 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b50d57ad-7919-34c1-8e8c-70a01de7019a | -22.5333 | -47.01812 | 2026-08-07 04:12:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b4b4b63-c14d-3caf-9b79-0d6fcf050fe8 | -21.87259 | -41.62359 | 2026-08-07 04:12:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a5335985-367b-386f-9349-0cdd08ead486 | -20.66263 | -40.97874 | 2026-08-07 04:12:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd6daafe-f810-33ba-98c2-b4505b9f2a13 | -22.53464 | -43.5563 | 2026-08-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| afdafe0d-d4a8-3ea7-af22-cd397e1c3879 | -19.82979 | -40.24504 | 2026-08-07 04:12:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d9884e7-14a9-3166-a541-65aa7d269afb | -19.7149 | -48.13274 | 2026-08-07 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 23a402d1-4da4-3461-869a-32a75fa9f0ba | -17.48281 | -53.32853 | 2026-08-07 04:12:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| df31a442-056a-31c5-8fa1-c804ac32848e | -22.45485 | -43.13297 | 2026-08-07 04:12:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 03a598e3-2b8a-3b46-be8e-57b083585dd2 | -22.89016 | -43.5398 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9b4eccd2-152e-3cb7-ab41-619a53c98150 | -19.69941 | -40.3082 | 2026-08-07 04:12:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7d1f3f1-739f-32a1-84ea-1e0d4a39c6a7 | -19.79794 | -46.38072 | 2026-08-07 04:12:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 833ce946-191c-3ebc-94b9-0223e7ef6bb5 | -22.53408 | -43.56013 | 2026-08-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 0fd24521-eda9-3f93-bab7-29d6a6767adc | -22.45883 | -43.1298 | 2026-08-07 04:12:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22822b9d-c1ad-34a1-9223-1e1837929b57 | -22.88174 | -43.01296 | 2026-08-07 04:12:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab8568c1-8418-3081-a6bc-d4cca7ee29b7 | -22.53125 | -43.55554 | 2026-08-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8a832ac8-d6ac-3cd0-afbd-47bd34eb9d24 | -22.74948 | -43.52133 | 2026-08-07 04:12:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 23cecc2f-6bd7-348a-addb-60533a35714c | -19.95236 | -44.70492 | 2026-08-07 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7ffac47-2c31-3ce2-a5ee-8d5c18b404ec | -22.5307 | -43.5594 | 2026-08-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| af8aba9c-619b-38fe-820b-b5793b093ecd | -22.91196 | -43.31389 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 59cfe134-ff79-3ca4-93b2-12356b209eba | -22.91138 | -43.31792 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 37b6aa1e-0e3b-3f34-b15e-a0873473e0eb | -22.54142 | -42.68876 | 2026-08-07 04:12:00 | NOAA-21 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4826d0c-a2ad-3b55-a33e-c00413aa0241 | -21.85644 | -42.05268 | 2026-08-07 04:12:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 25b8263b-c473-3f74-be85-6cd313a2575f | -20.70026 | -44.14872 | 2026-08-07 04:12:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f2fd623-a7c7-365d-8b12-f035033bfe92 | -18.63274 | -44.62076 | 2026-08-07 04:12:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3458439-8000-315c-929d-3356a39227bf | -22.53013 | -43.5633 | 2026-08-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6413fbb1-2060-34fe-8591-fac720b4f812 | -21.634 | -43.66388 | 2026-08-07 04:12:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 896bc7cc-e637-3d9f-8626-52283c2011ee | -19.56882 | -46.95327 | 2026-08-07 04:12:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 940399ca-9c5b-329d-96ba-d582fc108bbe | -22.92968 | -43.28843 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b479f55b-55aa-3906-9d77-60b2fff4a269 | -19.56769 | -46.95271 | 2026-08-07 04:12:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d118a3f8-415c-3878-a49c-885e2b73ccd7 | -20.38751 | -49.31163 | 2026-08-07 04:12:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4a4d01e2-bd32-3958-82a8-136622a8e53d | -17.4835 | -53.32513 | 2026-08-07 04:12:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 05e6b88b-5b97-3cfe-b666-698a1c2e79b0 | -21.8692 | -43.00122 | 2026-08-07 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ab035b4-b642-3c22-ad4c-6c61550ee2f3 | -22.90491 | -43.46163 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90ad54ea-a7b6-3e83-9bee-c976e101e8cb | -22.42488 | -42.27808 | 2026-08-07 04:12:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fd9d3e3a-f97a-3264-9369-626bf043c71e | -22.71929 | -43.82707 | 2026-08-07 04:12:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 11a4691a-0244-3722-8293-03bd1a1f5666 | -22.71648 | -43.82254 | 2026-08-07 04:12:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9687b257-6775-3952-8e0c-a9be13748689 | -21.63793 | -43.66063 | 2026-08-07 04:12:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7189c48b-ac63-3951-a130-67e6392dc646 | -19.7141 | -48.13721 | 2026-08-07 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ab3a82d-aade-3cfb-959d-e85f945e6b76 | -22.92409 | -48.69889 | 2026-08-07 04:12:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de011bd3-997a-3272-8247-601aa3c16d29 | -22.42845 | -42.27863 | 2026-08-07 04:12:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 59a1e9e2-2b33-3a71-b6e9-168c3630cee4 | -19.70763 | -48.13145 | 2026-08-07 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcca8789-cfd0-3b56-8c69-76a880ae565f | -19.69882 | -40.30445 | 2026-08-07 04:12:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33a509fb-0c73-3fae-82cc-054b7c75e856 | -22.53802 | -43.55701 | 2026-08-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8043fac6-c568-355f-8e9c-aeaecbef79bf | -21.44818 | -43.77996 | 2026-08-07 04:12:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 33f9749d-99b1-3549-ac2f-b91dec6c83f1 | -18.14997 | -47.98043 | 2026-08-07 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26824bc5-b35b-370a-8b63-7766e4dae173 | -18.00043 | -47.14151 | 2026-08-07 04:12:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c07faec9-537c-37e9-883d-35b5f14b9c1d | -22.88674 | -43.53925 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 37e216af-55e4-3a3d-96d5-ace894314d0a | -21.87624 | -41.62417 | 2026-08-07 04:12:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9067c8ea-9c4a-3e46-b3fb-b5907a893cc2 | -21.50385 | -45.52091 | 2026-08-07 04:12:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14c9bfd0-220c-3e39-a9b3-80fb70d0b316 | -22.91482 | -43.31856 | 2026-08-07 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 12b11590-8e5e-3606-9760-e8ec5012599b | -18.14917 | -47.98502 | 2026-08-07 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37df9095-d105-372e-b9a5-e17535b5cf42 | -17.47844 | -53.32355 | 2026-08-07 04:12:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b15b3d75-96a4-3e0b-9a56-dab1bbdb4069 | -20.58374 | -42.20803 | 2026-08-07 04:12:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e45a0c6b-ca0d-3549-98c0-ea478737e13f | -18.1455 | -47.98428 | 2026-08-07 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb20327b-6c8b-3db2-ad4b-feab82c82898 | -11.1447 | -44.4632 | 2026-08-07 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 3aa86a39-b70a-34d2-8771-5b83e5a1fa49 | -11.1443 | -44.4865 | 2026-08-07 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 977e1801-9a6a-3403-9d5a-b933f4dee12b | -11.1447 | -44.4632 | 2026-08-07 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| eecc6a91-7472-3700-b557-375da4fc80c3 | -11.1443 | -44.4865 | 2026-08-07 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 741e23c7-bc5b-3614-b708-2f29abf9e7d1 | -15.0785 | -53.5737 | 2026-08-07 04:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5e392cb2-5365-3105-a714-2af6d64b7af8 | -15.0975 | -53.5922 | 2026-08-07 04:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 50826deb-aa33-3afd-ba21-5a7ecb04219c | -15.0781 | -53.5947 | 2026-08-07 04:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 0394401b-a16b-320d-8b28-73ffe798dd6d | -11.1443 | -44.4865 | 2026-08-07 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| baa17935-003b-33fe-afaf-f685165a854c | -2.69173 | -47.35844 | 2026-08-07 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f4ec6c3-6e9b-3b8f-85ad-d50007c73869 | -2.41651 | -48.6333 | 2026-08-07 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ff728f-5889-3e75-b485-2e86af0cc080 | -2.02906 | -50.07564 | 2026-08-07 04:42:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ef66c8a-bf8d-3f1d-922d-a1ca6c426e95 | -2.48701 | -49.32905 | 2026-08-07 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 468b2a18-100d-3ebb-a4c2-c28d33a21abd | -2.48414 | -49.32471 | 2026-08-07 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71eeb339-494c-3edc-9ba2-18f723328d41 | -2.47661 | -49.3274 | 2026-08-07 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e15c0c2d-072b-3338-a986-ffd6f4158654 | -2.6945 | -47.3624 | 2026-08-07 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcec08b8-b49b-3026-aa38-9b4425c36a36 | -2.69504 | -47.35896 | 2026-08-07 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a1e89de-a45c-38c1-9e6a-72a272c17bb2 | -2.48068 | -49.32416 | 2026-08-07 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04b4df45-cad7-320e-a431-275015e16539 | -2.48007 | -49.32795 | 2026-08-07 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd761dad-5fee-3c2a-9ddd-79b97692a5ce | -2.4199 | -48.63383 | 2026-08-07 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adcf9353-a110-3a36-9091-db5af447c003 | -2.69118 | -47.36188 | 2026-08-07 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad774682-e042-3233-879c-79bbcc5b399d | -2.48354 | -49.3285 | 2026-08-07 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7943ad74-ccba-3190-9333-899d4ccef131 | -4.36602 | -47.77181 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c57e78f-0e16-3baf-96bf-931eb8ed1981 | -6.54966 | -56.25278 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 508a49ab-1150-3b13-b36a-9045f867aed9 | -3.12199 | -48.58904 | 2026-08-07 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dd26c99-9844-349b-b2a9-5852a7038022 | -6.85743 | -46.0041 | 2026-08-07 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b12f30e7-a700-363b-855b-dbf3d1648a37 | -8.02327 | -55.11872 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 072de029-8165-3c02-845e-d2fc65af667b | -2.94577 | -50.31583 | 2026-08-07 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b9d03db-1894-391b-9f56-eb870ec89f27 | -6.71193 | -58.95881 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8684c3cb-43d3-315c-9cf9-5d436a95eb9c | -3.96098 | -43.10758 | 2026-08-07 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 550d16c1-f8a5-3e41-8ee0-96212687d383 | -10.2467 | -49.25446 | 2026-08-07 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cfe5956-72bb-3b06-a8f1-f48ac87e270f | -6.71678 | -58.9327 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537a868a-8363-32b4-aa56-aa15e53d550b | -2.81646 | -52.29213 | 2026-08-07 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfc69bee-9d2f-38b6-b65f-dc3423531655 | -6.0625 | -44.886 | 2026-08-07 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13ae2867-4af1-381d-8cc6-f57ec54b47b9 | -6.7275 | -58.58693 | 2026-08-07 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 114b57de-2fe8-357a-8767-7f1366a95e71 | -7.03836 | -56.51029 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a32c47d8-b37f-392d-bef8-183aabe459d7 | -10.12538 | -48.91194 | 2026-08-07 04:44:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fabd2307-ba38-3fc4-9ba2-901f1847a3d1 | -6.71854 | -46.18348 | 2026-08-07 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8555244c-db24-3712-a31e-c4f697fb5360 | -6.06708 | -49.48882 | 2026-08-07 04:44:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 578b0a17-3287-3a37-b833-080cccdc68e6 | -3.26758 | -49.53019 | 2026-08-07 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c5c285a-11f7-373f-90b4-5e7d6bc6f2df | -6.52802 | -56.54793 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 068dd3cd-e979-3b12-8c7d-36ca1f0c9b68 | -6.61565 | -56.34615 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
