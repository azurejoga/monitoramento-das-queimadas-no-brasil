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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4139500-2914-38ca-9472-068c6c37f266 | -7.81813 | -46.41082 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e4de4da-7407-37be-87d4-d5a4c6d014ec | -3.86445 | -55.69042 | 2025-10-29 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06a85dd3-0ba7-3b66-9162-ffaacabf6921 | -5.75422 | -43.39754 | 2025-10-29 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa05496d-4f68-3851-8e96-5e5c0b957185 | -4.08742 | -46.93921 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 084acabf-25d1-351e-afb7-2c13951e7f8c | -6.14414 | -41.57359 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb887cf6-a1d5-34db-a301-b8c67dfc8b47 | -8.55015 | -45.6974 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3666eba-68ad-3d5b-87ba-9e3d8baa2d08 | -5.41538 | -45.21449 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc1d71d9-e385-38a8-9718-19e314419880 | -7.80086 | -46.44508 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f5271d49-512c-37a3-86c9-d3b65328ab62 | -7.08298 | -44.94186 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 804690d3-1c2d-32e7-bd06-feb0db8b4ce1 | -5.20032 | -46.14937 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b80a85a-f763-3608-9378-72cb153aeed2 | -3.09994 | -51.2791 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 200e2235-4dd3-34c4-a670-7271c81efd1e | -7.44034 | -46.60603 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c98a2a7-d050-314c-89ed-17f0235b1d01 | -6.14488 | -41.68834 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69dc80ba-f5b6-35fc-b7a4-9f0e5dde9418 | -6.15866 | -41.82391 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19e1a890-d8f3-3190-a3fa-94ad827a0627 | -8.00217 | -46.21094 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 92190651-0552-37e7-8c15-6d07ff19781e | -4.67208 | -50.96698 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bff58ac4-f31e-3c3a-8025-8e8b75658e4d | -7.81889 | -46.40569 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f69697f-95a1-31d0-8103-6bee20efa3c1 | -7.49192 | -47.03954 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2c7d234-3225-3e2e-a255-38fa48d55a76 | -3.70728 | -45.39102 | 2025-10-29 04:44:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17319f4b-871f-39ba-a63f-b6686f001e26 | -8.69234 | -47.13121 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff587c3-139f-3192-93f7-a78881a98592 | -8.55124 | -45.68982 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf70a8be-5ad7-31d1-b290-99174a473198 | -4.20523 | -50.09225 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d87661c-5a5f-33e1-a15a-78e0f731a739 | -4.00371 | -49.21213 | 2025-10-29 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1094199-5aa4-34fe-9b4d-0d71724b495e | -8.69407 | -47.13405 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d381d5b2-21d8-31da-8867-fe29bff79d49 | -7.34221 | -42.47816 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 063cf098-abd1-3e12-b9d5-fff32a7103dc | -2.14839 | -52.58321 | 2025-10-29 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 539dd0e5-8445-37eb-a2ad-98aedaf0b47d | -4.7313 | -44.44906 | 2025-10-29 04:44:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80a99385-988e-35b0-998c-ff3791884d12 | -4.6603 | -46.3998 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c24e388-e6fc-3b0e-9e9b-283a2f9f8c36 | -6.29615 | -41.87771 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 55d3e560-0324-36b7-9b4c-7cb5e2115f19 | -3.54693 | -54.69232 | 2025-10-29 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb6760e-fd47-30c4-810c-c830a47a5260 | -7.07448 | -44.95816 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fd0c4e2f-1525-3a41-917a-3b09295c461e | -7.45299 | -49.41006 | 2025-10-29 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9c94d4f-9da8-3733-8e5f-4a1f3e8863ee | -7.12484 | -46.98355 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0aa4308-b643-32c4-a3b4-47ead73b5ce9 | -7.75234 | -46.50005 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a333eaf3-38e7-3710-af20-7bd0ca7c16e1 | -8.51194 | -48.27965 | 2025-10-29 04:44:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7997c924-2e34-31d4-b9af-b8bc55e0b01d | -5.35034 | -45.36514 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a75a70cf-9a4c-3192-950d-153cff03dd42 | -8.40269 | -46.93073 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c74f68d-c5c9-309b-89e6-290d088aaaa5 | -3.58496 | -53.53458 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41626c46-339a-3932-98db-e409d4fc1da0 | -7.3225 | -44.73885 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ce62797-1917-3669-9921-94af151a4994 | -5.85604 | -47.70025 | 2025-10-29 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af48b3c9-1821-3894-96ab-5495405a6c14 | -4.20301 | -50.08485 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e30382-a938-3e52-ad4c-b23d9709ffb3 | -8.55381 | -45.70179 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c4c73de-c24e-3629-8416-561a1c25720b | -7.42622 | -41.86117 | 2025-10-29 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0c005cb1-6980-3d06-817c-e7f9ec4db1b0 | -3.12747 | -49.10222 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fc48c11-4924-3029-a713-0013d2ab9e1c | -5.48816 | -42.16711 | 2025-10-29 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 392836ed-a0b3-3a97-ac96-c36c7d1bec63 | -7.80653 | -46.46148 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b2817b87-0e95-30dc-b89e-7266eb86ef0f | -3.33865 | -44.19947 | 2025-10-29 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4368ab94-6d45-3b4c-8862-0fff61afe376 | -6.77221 | -46.38316 | 2025-10-29 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbe743f3-f455-33ff-92ad-e083e859be40 | -3.04601 | -50.26912 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e2975d1-b32e-3a67-bd9d-70b2d339202d | -2.20213 | -51.36767 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 70525ea8-29fa-3715-aa62-dc084db3eda5 | -7.2023 | -44.15808 | 2025-10-29 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66aa06cf-ac94-35f3-b953-f452a7a6f366 | -4.37521 | -48.67629 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5273fda1-ac06-3d30-96d5-ebe51c54dbf3 | -7.94998 | -47.84364 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4626b9f-bdf2-3563-8e77-945622da70da | -3.95012 | -49.90071 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38244038-a792-3d6c-8bea-d90a1f83846c | -4.01206 | -43.23723 | 2025-10-29 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d603a1f8-9eda-36d3-b9cc-8faaf9fc6d64 | -7.12451 | -47.01221 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bf11d9e-fb6f-34b3-b544-676a84ad55e6 | -3.14525 | -53.14421 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f6055a-a9de-3ef7-8608-08992b150c60 | -4.35554 | -43.64135 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9492ac0f-27cb-3037-b91b-9dab4fe1a200 | -8.03028 | -47.39863 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dc77455-450e-3bc5-8693-e653732d9bea | -5.56843 | -42.1735 | 2025-10-29 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0401b577-5ba0-3c2d-a928-a2f226442845 | -2.06754 | -48.14758 | 2025-10-29 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a94938de-ae1c-3675-b10a-e65dd94579f0 | -4.32219 | -55.61851 | 2025-10-29 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 784d0468-8a1b-356b-a7fb-a84febb89ce7 | -8.21265 | -43.80741 | 2025-10-29 04:44:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48de415d-8b84-3956-8896-b95d50fab468 | -7.12676 | -47.20468 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea0edc36-61ff-30f6-a3ba-7c7c663f4435 | -7.98589 | -45.53953 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d57e58c0-5235-327c-ac46-ecf11dc9cb7b | -8.26379 | -46.35001 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c4c2c50-5940-34e3-a752-af014f4c3082 | -6.10987 | -42.42852 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 57c1700d-0013-3e2f-bad8-e60658809d79 | -4.32209 | -55.61827 | 2025-10-29 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d48faee-45f6-30ea-8c32-8abab6677ccf | -8.03203 | -47.4129 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f45dfe58-c0ac-3427-b7b0-580d520caa16 | -7.80867 | -46.41979 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cb1742f-5c39-340d-b4d5-30828dfd8ce6 | -4.43374 | -48.00821 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bb0889c-37ce-3753-a973-c8b1ea43fb20 | -4.20409 | -50.07795 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b65683a-b026-3631-a1fe-26b4afedf579 | -7.92236 | -45.70734 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6669c82d-7cf2-3d2a-b032-bb6d5e4ac964 | -4.21914 | -50.15442 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75350b8e-696d-3011-83b2-01cc55bb101f | -7.24407 | -49.40148 | 2025-10-29 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a1e692b-9ec1-3370-a543-b75b6f6c2428 | -8.0327 | -47.40832 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe8a6b5d-86ae-379e-a66d-bcce8c3f1083 | -3.80093 | -51.10279 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19b7dc74-0a0a-3e5f-a85c-b28b8a8c689d | -6.10943 | -42.43155 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 883547a5-a264-3d99-82a1-22d9dc529433 | -7.49987 | -46.74765 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b83d67d-944d-3f0c-8a8d-1a7433fc6d44 | -9.24164 | -45.57158 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b9d87c3-de9d-3a0b-b566-000e76c9e73a | -5.59149 | -51.12672 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0b94f1e-b57b-3ada-9f3c-56820f0b1042 | -3.0381 | -49.52053 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80c89947-3438-3280-8198-2f374901e6c0 | -6.49015 | -42.24254 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 588c3b7b-51bd-33ec-9368-54fa315a2e18 | -7.44351 | -46.61156 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2aba449f-1ea0-3e4f-97fd-280219cc3b26 | -3.04913 | -49.51515 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f3bbd12-93e1-3e78-b1b8-49e091de1d7d | -3.43988 | -50.22575 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a12741ec-effd-30e0-ba6f-11133312d7cf | -4.13015 | -48.74397 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f3ffee-a2c6-3071-b42b-e15ea8696b17 | -7.93161 | -45.4976 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4277752e-6d39-3d96-b662-801c4eb0a4c6 | -5.59636 | -46.2357 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 649b8cd8-3abd-3d9a-9042-0cfca50778b4 | -3.38412 | -50.15018 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abec4ba3-7974-3ef1-b2f4-80c671b7729d | -2.4255 | -49.31122 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f32f1cd0-8241-3938-9bf6-e71c11ffee5c | -5.85667 | -47.69612 | 2025-10-29 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f907f3b5-6015-39e0-a280-903b6c2ef3f6 | -4.20794 | -50.07502 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a9b8950-b709-392f-a0f2-97d0c7d80786 | -2.42218 | -49.3107 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36011fa9-bf4d-3b66-8d57-5dd8f48bf139 | -8.11758 | -45.49434 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bf426d2-1fc4-38ec-862e-5b6d8c5b5b3e | -4.21456 | -50.07605 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76b3e269-c77b-32b8-b3e3-4d7aede5de7c | -6.1324 | -41.85715 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 138f8962-874e-3bb7-a885-071c19f83816 | -5.11636 | -49.26673 | 2025-10-29 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45fa0523-0656-3157-8d2a-7e8ccb77f54a | -5.62024 | -47.11118 | 2025-10-29 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f25ed6f-6265-3a4d-82f3-174d3c8f8c22 | -7.27708 | -46.89762 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README66.md)
