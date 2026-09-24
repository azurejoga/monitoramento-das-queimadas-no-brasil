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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9598c7f3-9c15-373f-bd4b-9c123d5942fb | -9.47603 | -40.32768 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 13abdf30-c283-3120-8d00-ca54dad47790 | -11.68207 | -50.1862 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89a08a03-2be8-3cc5-b62d-d55cc0ea3dbb | -8.90342 | -45.91063 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b9493b4-7464-3023-9c14-0a16498733ee | -8.90403 | -45.90669 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76a9e6f1-5c4d-337e-83f9-163396037591 | -12.04401 | -50.28323 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0713cb5d-f7f9-393a-ac32-db73acb4cd91 | -6.61396 | -59.93734 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 53e1c9a2-9050-3ded-a08d-b7a47377073c | -6.06986 | -57.80104 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1624d713-6ca9-3311-b570-a7243e481341 | -13.45925 | -46.25542 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9d0da94c-23ab-3f57-943b-366a2292c2bb | -10.42072 | -49.37424 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 788d2505-aa09-3454-ab50-24a91a2c4819 | -12.13953 | -45.62205 | 2026-09-24 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78090384-ce58-36f0-91ad-0b978b743a02 | -5.86075 | -60.16078 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8439c776-01c9-3291-bc0a-b1b2ced1198a | -10.21312 | -44.14285 | 2026-09-24 04:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b84c60a7-301c-3405-a750-717bcc1fb750 | -8.45992 | -48.69562 | 2026-09-24 04:46:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e420494d-d406-37d2-816d-5fd226ce14ab | -6.61711 | -59.9179 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7e9b312-1d1e-356e-8aa8-31880e133826 | -6.43711 | -59.95395 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 16bda6e8-df8b-3364-806a-50269b717596 | -6.66958 | -58.5847 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4e6cdc1-8894-3bfd-ac66-debf02400c68 | -13.07629 | -47.39993 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d4d5389-f9c8-3bf7-b970-20bd160c3464 | -11.63029 | -50.61341 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13c60a80-fcd8-34a3-b58e-67f1c62faac2 | -11.22942 | -51.38797 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7213cd2-df46-3c26-b01a-9b873e045bb7 | -10.83354 | -48.48432 | 2026-09-24 04:46:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab45a1c0-d7fa-3be6-8a92-bf746fa8063b | -11.45882 | -47.40077 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 260d14d8-adfb-3787-8d4c-dae09a5c932c | -9.26601 | -46.24634 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2ba3c62-7247-3a60-af5c-17cf73fae76b | -11.58531 | -47.73503 | 2026-09-24 04:46:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b989ceb-0e08-3117-a288-1557a1fe9a60 | -9.18302 | -46.51041 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3905797-cc68-3777-8447-292d12c738a6 | -12.11896 | -50.74404 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c390fe7e-4066-362c-bcfd-11722159eeb9 | -11.48678 | -47.35534 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 129a7af1-c303-3422-ab02-5aaad27c88fd | -11.40084 | -47.39221 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9db70fac-b3b5-32c2-8ff6-480c83c379ae | -11.22855 | -51.37163 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecbc7f2a-c47a-3b71-b83b-a097e5050948 | -12.01785 | -47.80237 | 2026-09-24 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b7c01ed-d8b7-3fb6-b95a-3eff033d0e7a | -12.14218 | -50.7518 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6c18b336-8499-3723-b441-787d1ff925b0 | -12.6756 | -45.02812 | 2026-09-24 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ea17f6d-e18b-3581-906e-035eb1c279fe | -10.07199 | -46.01546 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 006822d9-9455-32e9-beb8-0242c1437ca0 | -9.74593 | -48.34651 | 2026-09-24 04:46:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74728e81-ed6b-32d7-b12b-5220b00196cc | -6.61516 | -59.92851 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ebc46207-d02a-399d-9a77-03644950e010 | -10.90416 | -53.95008 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54d0247d-4773-3cf5-87e1-99cb2cc04921 | -12.1703 | -47.37519 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cf21101-3fb1-3d79-9a1d-6bb3de30e2de | -7.03904 | -51.39293 | 2026-09-24 04:46:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4088834-a29e-3f6c-a989-097b3488432f | -12.69875 | -46.99284 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4be1ea38-5dd0-36e9-b06a-739808eef793 | -9.14981 | -40.11106 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1f91a64-2da6-3949-9661-d86db8633f09 | -11.25929 | -40.93226 | 2026-09-24 04:46:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7742194c-8be5-3ac3-b887-9605fadefa13 | -9.26194 | -46.24965 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7d1c609-8dcb-3728-b968-a1e4cc177220 | -11.94443 | -50.74099 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 954afbed-359c-3bcb-9092-37f592e86c17 | -10.70208 | -48.71951 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab40bc2a-0e2e-3f2f-83de-75a8e2119694 | -11.86368 | -49.95417 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d3dcde5-759c-3678-af6c-f64f28d34e6d | -6.43629 | -59.95901 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6512494d-8d01-3107-97d7-ad8ecb89abaf | -5.59988 | -60.20102 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab4490b9-e6f1-3fd4-9398-0125cb694bb3 | -10.39131 | -46.56586 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8742af21-e628-3225-9bba-48273c7110b2 | -12.12177 | -47.3751 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82f7c3fc-458d-3814-ba2d-26bb8474eec8 | -12.3752 | -47.08292 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26893964-b2f1-3038-a021-7a5ffa417579 | -12.28861 | -46.39514 | 2026-09-24 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34dc6a0e-817c-3989-88d7-8c5fc5f1a20a | -9.48084 | -56.76075 | 2026-09-24 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c232ba0d-a05f-3a3a-8186-9368fc112370 | -11.69719 | -44.49098 | 2026-09-24 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7063386-61b6-3247-8508-99a4eeff0534 | -9.47444 | -40.33922 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| a0585eb3-0c36-347b-a744-effd25748639 | -11.10687 | -48.29658 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93613a2b-4adc-3f73-a1a3-4bf0f15210ac | -6.66524 | -58.57493 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f385f751-559e-3f6f-a6f2-1a9610c70923 | -10.91286 | -53.94791 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8f7a664-8bfd-36e0-98d5-bb187d8f3122 | -14.63387 | -50.59719 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afdc328a-cff3-3998-906e-9288b9a2b9be | -10.27475 | -49.96972 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e004fbab-86b1-3f78-90cf-f74e382caf8b | -6.44161 | -59.9655 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b952bc57-a825-367a-9c1d-3168cbcb5484 | -6.09135 | -57.63169 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22945b9c-3b3d-3a39-8268-d379cb3b0acf | -10.27812 | -49.97028 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de5e7b85-25c9-3828-b2b0-e7173b966bad | -8.12989 | -54.8182 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 989fbcf1-ca23-32f8-962e-c3aac7712444 | -14.64392 | -50.59893 | 2026-09-24 04:46:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0f8dcf1-2099-3ccb-8a45-aaa8428c31d4 | -11.9311 | -50.73946 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39576b27-6931-3b4e-84bd-53c357bf4ac3 | -12.12357 | -50.7372 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d4e0ea88-9974-3e10-be1e-c4c3cab5a5f6 | -6.11049 | -59.88097 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b84094d7-43af-3e20-8249-75d26968a8af | -8.2651 | -54.76683 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e076a73-cdda-334c-8a09-d4d5598bb184 | -12.42028 | -46.95819 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b891afc-a59e-3998-b201-d098cc2f5ffc | -10.41397 | -49.36201 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4491d508-504d-3d88-8163-dcb87553ad41 | -13.06946 | -43.28286 | 2026-09-24 04:46:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b3f6e0c1-73be-32fc-bb43-64dddb17a759 | -7.43894 | -49.83374 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec9bdca0-94b9-318a-966b-a9957afa3781 | -10.92508 | -43.85334 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca99a584-3d93-3b8b-b760-cb912cbad5d0 | -12.13938 | -50.74751 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d570118b-2aee-3240-9a30-d9e47bfa154e | -6.66013 | -58.5695 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 122c2bd5-2cce-3c1d-b4d6-a3b657847f8f | -6.4579 | -55.00838 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a8c986f-b662-3708-917b-d2be0c6ff1cd | -11.6574 | -43.48936 | 2026-09-24 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8dca6b4f-1f8a-3bb1-b6ab-c39d94164cf9 | -13.9381 | -47.82433 | 2026-09-24 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0102853-35c4-3c43-8c8d-d65b96a9c72a | -7.41868 | -49.83076 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bdcd693-6b9d-35f0-bc5e-54e772878081 | -9.84005 | -48.50167 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bba72fa-3dc8-323e-95b8-30247bec7d67 | -11.62811 | -50.60544 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 383347c5-c253-306d-aef5-87539167c976 | -11.12578 | -48.30693 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7816affa-3281-3f3b-8d31-996c3412aff6 | -11.95962 | -50.75502 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dc75482-4b35-301a-bb48-57b55c0c9bfe | -11.62872 | -50.60175 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b0b84be2-f428-3ec8-b09c-5a85c257f9f4 | -12.10936 | -50.73859 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d08b869-8e1c-3d5b-ad14-39692415691b | -9.25559 | -46.24455 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 39dbc05d-5952-3642-93e6-858b54acde2a | -12.41795 | -46.94987 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9ebd7e8-9da3-3908-9cfb-04bed90a1571 | -11.59833 | -58.50941 | 2026-09-24 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f7421d3-85bd-3fe4-8703-caaa05343dad | -7.42925 | -49.82861 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 652effa5-1094-329e-acba-ab62586637c6 | -10.62282 | -53.98816 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d64736b7-3c44-3d2f-b443-e1b21d0256ca | -6.615 | -59.93186 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e8c44c9-2ca8-3ae2-97fc-bb342f3ed5b1 | -7.44173 | -49.83815 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cffa5cb3-cb82-383c-b920-c628cb3aa83f | -10.61423 | -48.95033 | 2026-09-24 04:46:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbbb1494-9055-3eec-9af8-2be6770c48e4 | -9.99797 | -45.19353 | 2026-09-24 04:46:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c5d4600-061e-3123-944e-42bcb7724f86 | -12.41897 | -46.95887 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01412d85-42bd-3edf-8b77-40e86a6b5bf8 | -10.61751 | -53.99467 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8c833fa-2273-39ed-86d5-22832530a3b7 | -8.25991 | -54.77028 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb832af4-874c-3801-85f5-588b7d324dab | -11.91467 | -50.73285 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8c0f273-d3c6-38f2-bcf6-9ae51642e627 | -11.49685 | -42.33346 | 2026-09-24 04:46:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2dbdc44-30c1-3446-8994-5eddb2f284a7 | -10.26976 | -49.95777 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 116e829b-f4b4-3aee-9ca4-5da7557f266d | -10.07416 | -46.01871 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README54.md)
