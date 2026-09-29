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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72d61be8-afcc-3604-869d-4f96b84c4c56 | -8.3617 | -45.4013 | 2026-09-29 15:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 350a306c-cd0b-3e9f-a1db-3c571f8f7b4d | -12.2703 | -50.2951 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 045bef42-0b15-3f08-8502-bd6c0efb64ed | -12.289 | -50.3143 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 771fc42b-67c9-39af-8491-af4414bfde76 | -12.0126 | -50.9464 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| d768ee55-ed56-3720-a8d4-841e087047c9 | -13.2253 | -51.5466 | 2026-09-29 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3f77fb1e-edc8-3989-8eb1-067db7e9a1f3 | -11.9939 | -50.9273 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 02321283-9cbd-33bd-8a60-07b2efc577f8 | -9.7874 | -44.8289 | 2026-09-29 15:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| ed01579b-949a-34ed-b953-bac5458d5a4f | 2.1082 | -50.8583 | 2026-09-29 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 11eaf9f1-eb53-3f8e-b64e-88f513dc3305 | -9.9787 | -50.1198 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c32dcb28-79ef-3a47-9d00-57129703e16b | -12.1547 | -50.3735 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 7552a029-01ea-3a83-90de-9666fa9ba709 | -10.8967 | -50.6866 | 2026-09-29 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| fc828581-1a3c-38b9-be4a-3c05ca5a7226 | -10.2376 | -50.5204 | 2026-09-29 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| da9652cd-e6fb-3f83-9fad-67be412705de | -11.7643 | -51.0173 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0f6e91e9-ffca-3027-a4f1-ef9aaaa3815f | -11.9936 | -50.9486 | 2026-09-29 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| aae64a12-36ed-3e9c-bb48-131a1e62fa01 | -12.2696 | -50.3381 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| a54b14de-46c9-3427-94ff-8f8cea2ff9a3 | -12.2887 | -50.3358 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 761f630b-6a9f-3043-8a5c-98d9db628c40 | -12.3088 | -50.2688 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5dff5ef1-5329-3024-b7b8-e445f7045b21 | -11.9964 | -50.7563 | 2026-09-29 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f8f10a6b-8888-3044-af4a-00846cb60775 | -11.5818 | -50.5047 | 2026-09-29 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| abdafefe-878d-31c9-a3aa-68bc40482da6 | -10.6035 | -49.9913 | 2026-09-29 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| fbb10723-0745-31da-92c1-a77aead03b14 | -10.2067 | -49.9898 | 2026-09-29 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a6cb699d-97bd-3c6c-8842-de86bc1211b2 | -2.43441 | -46.30742 | 2026-09-29 15:50:00 | NPP-375 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eb439a32-319b-3fb8-b762-411a3814d044 | -2.43498 | -46.30575 | 2026-09-29 15:50:00 | NPP-375 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5c3e3c38-ff14-378e-bccf-eeee03bf573b | -1.61442 | -46.00085 | 2026-09-29 15:50:00 | NPP-375 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0c769e94-b347-3201-b74f-f140538f33a1 | -1.61544 | -46.00762 | 2026-09-29 15:50:00 | NPP-375 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 91660da9-72ba-3072-bd44-63adc6e6c007 | -12.1734 | -50.3927 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5319dd1b-ef72-3ce3-a56e-6582fbb3369b | -10.2376 | -50.5204 | 2026-09-29 16:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5e99944b-53f4-35d3-b73d-2a433370057a | -1.4303 | -48.9102 | 2026-09-29 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 25b2311d-da08-3f8c-afed-f7a69bf3feb8 | -11.0991 | -51.1111 | 2026-09-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ce544365-ccf6-3932-bd4e-3a3ed26360e4 | -20.8369 | -57.7101 | 2026-09-29 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 125.0 |
| 9c6176e2-0567-367e-a2c4-b002d9f921dc | -11.7828 | -51.0578 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 81a95e96-f70c-3522-ba92-c92c72d9374d | -15.3998 | -47.9261 | 2026-09-29 16:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 124ab6de-0d8f-3244-b05d-aa7845740085 | -12.0126 | -50.9464 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| bed1184f-7137-320a-9238-a68daebe41dc | -11.9932 | -50.97 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 02e253af-82c3-37e2-aa1c-4d0cff151f51 | -11.9551 | -50.9743 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5227594b-1328-352c-be0f-ed02dcc58517 | -11.904 | -50.5746 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 11dfd226-f9c8-30bc-b6bf-f7a3e26cbd91 | -20.817 | -57.6919 | 2026-09-29 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 8b4e68dc-6866-38c0-ac9d-12a21d272748 | -9.977 | -50.248 | 2026-09-29 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d6be1c42-ada0-34fa-a3c3-1859b8b9b1c1 | -10.8967 | -50.6866 | 2026-09-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 1d8a6ade-8d0c-3a45-b15e-9c60eb760c4b | -12.3857 | -50.2379 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 987dd0e8-5c06-323a-85ab-96a683d238c2 | -9.9582 | -50.2499 | 2026-09-29 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| dc7b6369-3458-3a7d-9131-be5ecdc6f9eb | -20.8373 | -57.6891 | 2026-09-29 16:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 144.5 |
| 15da2844-de43-31ef-9073-309ec20757f7 | -6.9795 | -71.7732 | 2026-09-29 16:00:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 848.2 |
| 24d7f610-43b2-35e7-8ae0-9b37a675e84f | -11.7129 | -50.6394 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a186d670-a496-33b1-b119-6b836919dfeb | -11.5625 | -50.5283 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ecc0e0c8-851b-3036-9639-c24d5d17c3ce | -6.9795 | -71.755 | 2026-09-29 16:00:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 244.6 |
| 102f1561-568a-3cac-a74c-b47c48c48165 | -10.9864 | -49.6915 | 2026-09-29 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d47fe3aa-79be-365e-a142-4e3b2055ce45 | -11.751 | -50.6351 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 494c02a8-0181-36f2-a21e-4b657aabb871 | 2.1082 | -50.8583 | 2026-09-29 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 86.7 |
| df7cfc27-9184-3cf3-b32e-872437ce1180 | -12.3088 | -50.2688 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c77a4ee0-0b72-35b3-a0a6-137975e454f2 | -10.6889 | -50.6658 | 2026-09-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d5e8c1eb-ee1e-38fa-ad33-54c1783d2adb | -11.7132 | -50.618 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a6638717-d318-3e64-a1fd-ad2b25659f8a | -11.7322 | -50.6158 | 2026-09-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ee12b36c-2f4b-3345-a60b-a3d8137e2d49 | -10.6505 | -50.7123 | 2026-09-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 312d3c46-0e41-3d7f-9861-eaaa7813656e | -12.0129 | -50.9251 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 099823d6-b293-3a5e-8289-2f2bfa93583a | 2.1266 | -50.8788 | 2026-09-29 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a2870ea6-4692-30ef-a7cc-71ccc1193922 | -11.8802 | -50.8977 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 12721c2f-5697-320e-8b3f-f6a2ca233398 | 1.2613 | -50.6845 | 2026-09-29 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| beef3450-6cc6-3c57-b46d-cc9e971e4634 | -1.4672 | -48.931 | 2026-09-29 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f590f659-147f-363b-a435-71ffa7c00159 | -11.8989 | -50.9169 | 2026-09-29 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 14d79b4b-fbe2-33e6-8594-e1a871d3fe31 | -10.8967 | -50.6866 | 2026-09-29 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d5aa4e67-5d64-32f4-9f80-88991c92c852 | 2.1082 | -50.8583 | 2026-09-29 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 431cf32b-a63a-37f1-8595-85ac4a80e523 | 2.1266 | -50.8788 | 2026-09-29 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 5f59b8f6-4c54-335d-833d-cebed5fe1bef | -20.9159 | -57.8246 | 2026-09-29 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 130.7 |
| 9ff2c1cd-f361-31c9-b4eb-224962c442d3 | -11.7828 | -51.0578 | 2026-09-29 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 9776ef67-24e8-30bf-8935-158a0927658c | -11.8799 | -50.9191 | 2026-09-29 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| efc18b98-34fd-30b5-800a-b90f9d099fa8 | -11.8611 | -50.8999 | 2026-09-29 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 4a0011ca-2b60-3087-818c-d049bc1a45ed | -12.1547 | -50.3735 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 37d006bc-fc5b-363d-8fd8-d40618279f07 | -11.7129 | -50.6394 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| a0099737-b6ee-33a4-af42-dc1ca1c95c33 | -12.2897 | -50.2712 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f5bf5633-3788-332b-b94a-09dc2bd5fe1e | -15.3998 | -47.9261 | 2026-09-29 16:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 782ca33c-807e-3aa8-87fc-34f36cf20bac | -11.7325 | -50.5944 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| a0f4335a-8fda-3f52-b8a6-042307bf8b44 | -10.7426 | -50.8939 | 2026-09-29 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| cecd3675-cc55-3cb0-9135-66f4f64ab48c | -9.9396 | -50.2304 | 2026-09-29 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a4e39fde-d01e-33a2-b08c-993eb18990bd | -10.9154 | -50.7059 | 2026-09-29 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2fd99fe9-9c04-3744-bfaa-f0a71e575337 | -1.4303 | -48.9102 | 2026-09-29 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 74c9014f-07dc-3b90-9d80-785012cd72c3 | -12.3088 | -50.2688 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3e1328e4-d022-327d-a9db-06e70e1d16c3 | 1.9241 | -50.8202 | 2026-09-29 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 417d30fd-bca0-3fba-b1cb-18a7ec8cfa38 | -11.9231 | -50.5724 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 66d91bed-667b-3270-8bec-7b733b0b4088 | -12.2508 | -50.3189 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 8e69a5d8-2e57-371f-bcc3-2136738777d4 | 1.9607 | -50.9028 | 2026-09-29 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a33c6deb-18f8-3d21-8057-76eecd53843e | -11.9939 | -50.9273 | 2026-09-29 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2e766a69-6037-30bd-910b-7f5b10f98754 | -11.8424 | -50.8807 | 2026-09-29 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b9cb32b7-8050-33dd-bfd3-cfc2f8997d04 | -10.6928 | -60.7322 | 2026-09-29 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 262ea7ae-966d-3882-b2b6-797d2977e18a | -11.751 | -50.6351 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 5f14236f-59cd-3c2a-8564-ddada19ab5c8 | -11.8989 | -50.9169 | 2026-09-29 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b1c64e39-2c12-3849-b65f-96aa0f58e19d | -12.0365 | -50.6233 | 2026-09-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| cf50aa0b-fd92-3d95-b1bb-c824042987c9 | -6.9795 | -71.7732 | 2026-09-29 16:10:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 969.7 |
| 09741942-398c-35bc-af45-7503d16f32a3 | -10.6035 | -49.9913 | 2026-09-29 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5a6ab96c-e58b-30d0-9cf0-c3bbe0ecaa6b | -12.49 | -44.96 | 2026-09-29 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77cf7279-2900-3817-83ab-3073b5fe800b | -11.92 | -51.05 | 2026-09-29 16:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7124f32-9a7b-34da-be7d-08be2aeba8f5 | -19.45 | -47.95 | 2026-09-29 16:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc9be51-b88b-3455-b352-fed0e30c7398 | -19.45 | -47.9 | 2026-09-29 16:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 653f96e0-e882-31cb-9660-1d0d46b7839f | -11.89 | -51.04 | 2026-09-29 16:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba0a01ab-d646-3d0d-a1b2-3b4645c19af6 | -11.45 | -43.49 | 2026-09-29 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e2cd4a3-292a-3a6f-8980-a6b31ed040a2 | -12.1744 | -50.3282 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9f65b840-b9f3-3f5b-b479-90b49ef03976 | -12.1741 | -50.3497 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 9d2a83b2-0c3f-3c39-8655-8465fd784cf4 | -10.9912 | -50.6978 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 33629ddc-2cc7-3a17-999a-003280b73661 | -15.1847 | -46.141 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 66243e14-2cbf-39a8-826c-8a37d770dd7e | -12.1553 | -50.3305 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |


[Clique aqui para ver as próximas entradas](README97.md)
