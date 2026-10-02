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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a301fad1-7f28-3002-bee2-bf4dfa1fdbb8 | -1.23407 | -49.0201 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| afd310a8-8c3d-360f-9d7d-a3b9b63e0c5b | -1.23318 | -49.01035 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 01a331c0-db1e-3e4a-a20e-e75fa3bae30d | -1.22644 | -49.01139 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5a98d1f3-57ac-3f21-8137-0a18bd225240 | -1.87101 | -48.27929 | 2026-10-02 15:56:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35871809-4d97-3b57-bd7c-0d3a6d7b8e01 | -4.34528 | -43.83528 | 2026-10-02 15:56:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96ab549c-b237-3b33-98a6-87ad231a4e25 | -2.48477 | -49.73227 | 2026-10-02 15:56:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 810efa65-c5d5-3347-8d32-fd99caae6ad7 | -6.35538 | -49.25311 | 2026-10-02 15:56:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9ff29792-2b72-3148-9cf8-e24469ad7101 | -5.74163 | -45.16155 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 91a0d730-bb61-38d4-a054-87c521856ca4 | -6.33071 | -43.362 | 2026-10-02 15:56:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 67ee446a-c089-3fb6-b83b-e447682c70e1 | -5.73564 | -45.15606 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0e5cc24f-aabf-3a0c-a815-d30333238270 | -5.09564 | -40.58521 | 2026-10-02 15:56:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 621896e1-d1f8-3a42-b775-017b7f033944 | -5.94556 | -43.65486 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 0adc2c0c-57b9-3dae-9aac-33ddf252cc20 | -6.36569 | -43.61305 | 2026-10-02 15:56:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 664237fd-7647-38e8-a134-7539db956dae | -6.29172 | -43.11588 | 2026-10-02 15:56:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3f5d0c15-0c7d-33ec-ba4b-8dc55a4719f4 | -2.05219 | -45.80552 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3ef79ef1-430e-34d5-85ab-8258d7185c4f | -5.73522 | -45.15303 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 42622a5e-98ea-3bbb-b777-b5516058ab46 | -7.20395 | -46.54626 | 2026-10-02 15:56:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2d012c12-3402-36bb-8c78-545bcb727ffb | -3.98167 | -41.51821 | 2026-10-02 15:56:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a012ff2c-a663-306b-8fd7-034faf772fa5 | -5.73825 | -45.13742 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 0af1be03-7918-39b3-ac91-9732373c3db9 | -3.93617 | -40.65858 | 2026-10-02 15:56:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 95574b4e-89a1-388d-b849-a8189f24ba26 | -2.13676 | -45.86151 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 37236797-971b-308b-b8c2-52e42150a34a | -6.24234 | -43.77451 | 2026-10-02 15:56:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3d6d1212-c870-3474-95ad-303bdb2d1f8c | -0.97833 | -47.50141 | 2026-10-02 15:56:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7ece6391-898f-3b25-923b-95b541b822f0 | -0.25106 | -48.48428 | 2026-10-02 15:56:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 407747ea-46a3-302f-9646-51da9dd469e9 | -5.88243 | -41.51856 | 2026-10-02 15:56:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2fddf8f7-19f2-31cb-b3fe-09818bc0734b | -5.75492 | -45.14456 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 61ed6554-eb76-358d-a055-01181ec5f3f4 | -1.23545 | -49.02473 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 1d466942-7cb3-3568-85c2-55682a712353 | -3.74929 | -44.6972 | 2026-10-02 15:56:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2bc6837a-c333-3db4-a977-4ce341e9413a | -3.98502 | -41.52013 | 2026-10-02 15:56:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| c8c7d541-b608-3641-97e5-6b5c7f690f22 | -6.31899 | -43.34473 | 2026-10-02 15:56:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 50b98df9-f646-3827-ac70-af987124e640 | -0.66422 | -47.29795 | 2026-10-02 15:56:00 | NOAA-21 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d92b99c9-8409-3749-b4bf-fe2099c39251 | -1.23263 | -49.01049 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c4a5b7f1-11d9-37e1-aa35-65a5fe537daa | -3.82915 | -38.7168 | 2026-10-02 15:56:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e9965730-d026-33f7-b0ba-0fc1d1b6dd70 | -5.7348 | -45.15009 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 6aae2b44-c233-31c2-bf09-4d02469e4369 | -5.82801 | -45.01098 | 2026-10-02 15:56:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e3eec487-28b6-3351-aefe-89f1e2c70ad6 | -1.23479 | -49.0249 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 4e1aea45-a463-3861-83bc-4e84c7877b37 | -0.78359 | -49.27444 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 90249191-468d-3ca4-8ef2-7149d3f4cf87 | -1.25792 | -49.30777 | 2026-10-02 15:56:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5920dbaf-cb14-3947-b873-d169a016a33d | -3.66896 | -38.98106 | 2026-10-02 15:56:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0fe299cb-6c76-3004-9724-160f4c0331cb | -5.75149 | -45.15728 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9c1710fc-8a85-3723-b00e-c19d1a0055eb | -1.12616 | -48.84697 | 2026-10-02 15:56:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7445cbe3-d4a5-3749-b160-c0360404c43f | -2.73924 | -45.77019 | 2026-10-02 15:56:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a283175b-7ca4-34c9-bbdb-b640797033a6 | -5.74508 | -45.14886 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| f4dec419-f3ad-38fd-a8a6-b4520928dedf | -6.24415 | -43.77119 | 2026-10-02 15:56:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 85a2961c-cb18-3f8a-aa9c-d69f89d805e7 | -2.97948 | -44.31403 | 2026-10-02 15:56:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ade96080-c52d-31b7-89ce-eb3ba3e74466 | -6.07012 | -44.80331 | 2026-10-02 15:56:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8c637eb-108f-3dda-9c91-1a75c1dba910 | -4.34499 | -46.29619 | 2026-10-02 15:56:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9cdeabcc-68d2-3051-b205-3d5e189f8af6 | -6.90793 | -43.96162 | 2026-10-02 15:56:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 625a454f-8fcd-3d10-823f-35565030a2ae | -2.9916 | -43.19382 | 2026-10-02 15:56:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c16a76ed-0197-354b-9585-608d7e84e2ae | -1.73059 | -47.40863 | 2026-10-02 15:56:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58b71f62-abe9-3dc7-b545-43474add0684 | -0.79608 | -49.27264 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| cf293693-fb9d-37e4-861c-e9cf67443ff6 | -5.74591 | -45.15482 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5b20b70c-a5e5-36aa-ba4a-2913366806b0 | -6.94719 | -45.23033 | 2026-10-02 15:56:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 14dd7711-254e-3557-89f1-9527b2a39c75 | -4.35039 | -46.29523 | 2026-10-02 15:56:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c3012fa6-297e-39a3-ad71-ed24cc4e03be | -6.62068 | -44.71851 | 2026-10-02 15:56:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 62ef7841-e7c1-35b0-97a6-66f432109016 | -2.14142 | -45.85779 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1e653219-5488-30c4-9835-9c6aad0ae198 | -5.95551 | -43.65839 | 2026-10-02 15:56:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 387a021f-d97a-3f90-b564-0bf07ae76b33 | -3.58701 | -45.48314 | 2026-10-02 15:56:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c9afae5f-1f6e-340d-8190-6dbd51fb1c20 | -1.4554 | -48.9049 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d7623ca-9c2b-3291-88f3-08b45c548617 | -5.88643 | -41.51801 | 2026-10-02 15:56:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 0fcf2c7d-e53e-3816-8bcc-57b780cf1d58 | -0.98312 | -47.45912 | 2026-10-02 15:56:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a0a46f7a-45dd-3bfc-b5ef-ca2395b26044 | 0.02965 | -51.19458 | 2026-10-02 15:58:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 25.1 |
| d8eb76b4-5edc-3f29-8c2d-a71348b8c364 | 2.55956 | -50.96428 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7f886b8b-a74c-30b6-8008-1a5f74b60661 | 3.48388 | -51.45845 | 2026-10-02 15:58:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d22edb3-42e4-3112-845b-c0b83b1f42a1 | 2.65179 | -51.33358 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 0f26b3a4-ce90-318b-902c-9045bd8b28b1 | 2.53431 | -50.96167 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d475d773-53a2-323e-94cb-9dc6b586884c | 2.54169 | -50.94995 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7b54e421-ddaf-3be7-95c1-06d7cefec241 | 0.03013 | -51.1899 | 2026-10-02 15:58:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a0967d02-5760-36b9-a6a3-ca5c4455c8a5 | 0.03066 | -51.18806 | 2026-10-02 15:58:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 21.5 |
| d4b3ea3d-86cb-3b1d-8c4b-4b3536e7d104 | 2.55859 | -50.96998 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2b462bd5-065c-3ed5-9133-b89dd95e12a2 | 1.84574 | -50.84586 | 2026-10-02 15:58:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 680138cc-34cd-3c9e-a562-3f1b65fb49e3 | 2.709 | -51.06161 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 794063a7-18ed-33a5-9713-a260feab8709 | 2.70999 | -51.05593 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8d9adc32-d38f-3e0a-9789-7f68bc52f370 | 0.02907 | -51.19642 | 2026-10-02 15:58:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7dc4d192-10d3-3fda-ae10-d897dc4627f3 | 2.55489 | -50.9519 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 44414148-4417-36dd-80c8-744a3a7b6bc1 | 2.64807 | -51.33345 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7f95b0cd-8eb6-36dc-9528-2ec577c1d697 | 1.84668 | -50.84019 | 2026-10-02 15:58:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 21.8 |
| fe9b1383-470b-3a2c-a2a1-3470c983b73c | 2.53523 | -50.95606 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f8138d2d-8170-372e-b9b2-4e1c9953c4c7 | 2.54275 | -50.95144 | 2026-10-02 15:58:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 6756f450-dc57-3082-b862-e86a720675c4 | 1.91497 | -50.90775 | 2026-10-02 15:58:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e6df7318-3db3-325b-952a-10c435571971 | -1.4303 | -48.9102 | 2026-10-02 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8228da88-2cc0-300a-b475-2586d2238b0e | -1.4303 | -48.9316 | 2026-10-02 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c0c88ff8-c432-3534-931f-a73f246d0c87 | -1.4672 | -48.9097 | 2026-10-02 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5adb8bae-537e-3a31-a81c-90fa7ef65e73 | 1.8037 | -55.6051 | 2026-10-02 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6b4690e0-889c-34ae-aa63-6f6feaa7f9d1 | -1.4487 | -48.9313 | 2026-10-02 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d63deb92-2248-331d-badd-dbb9dd8a6f0e | -0.8399 | -48.725 | 2026-10-02 16:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 03b3b110-dc77-3967-99e7-1f4f8bcbc5ab | -1.4672 | -48.931 | 2026-10-02 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 74490d92-9e1c-3c8e-a732-1b50052c2205 | 2.5502 | -50.9526 | 2026-10-02 16:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 112.4 |
| ac464002-189b-31d3-b859-01d66b39d8e2 | -0.8399 | -48.725 | 2026-10-02 16:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 40292e6d-93e9-3efc-8d20-ebd72d34629a | 1.8037 | -55.6051 | 2026-10-02 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| b1a9d88d-6cf8-352d-b2ac-896de2cf4a8a | -1.4303 | -48.9102 | 2026-10-02 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2c89e07e-cccd-35dd-9af4-0592178b5c8c | -1.3192 | -49.1249 | 2026-10-02 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9c915f58-5b0a-33ea-8dd0-d802320085ef | -1.1713 | -49.2969 | 2026-10-02 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d584477f-8b67-39ba-acfe-f775317cce45 | -15.02 | -40.98 | 2026-10-02 16:15:00 | MSG-03 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77711a9d-edde-310e-a9ac-0603df888842 | -11.47 | -43.4 | 2026-10-02 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74f4f73b-5b25-39fb-bb97-a870ae11d11e | -8.55 | -40.27 | 2026-10-02 16:15:00 | MSG-03 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ae1cb98a-d2d2-3a66-9ecf-01aebfd02cfc | -12.5 | -44.12 | 2026-10-02 16:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16901907-87e1-3222-b4ed-00b811977f1c | -11.32 | -44.28 | 2026-10-02 16:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a9fa091-d88a-3eee-a5bb-996628c4f031 | -11.51 | -43.55 | 2026-10-02 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee5d08a7-a69a-30d0-a7d0-a9fee2a4fb0e | -12.5 | -44.17 | 2026-10-02 16:15:00 | MSG-03 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README106.md)
