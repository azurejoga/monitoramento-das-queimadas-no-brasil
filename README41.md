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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cabeaae0-82ce-3370-8253-3e9a3c9bea57 | -6.19983 | -53.24976 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7479f135-f943-3f3a-8bf0-ba60cf9df7ef | -13.4742 | -46.83347 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 469dbeac-388f-3d52-b842-52d90f424d52 | -16.5497 | -42.34987 | 2025-09-06 04:17:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b7f75ca-c0c3-35f9-a484-90d463d606bb | -9.30464 | -45.412 | 2025-09-06 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cefddfea-3e49-3b48-b6c1-d76387d24337 | -8.43636 | -47.31834 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4692a9a-3f5f-3880-9a9e-12522a9e7564 | -6.4545 | -44.67392 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23329da8-55e3-38de-844d-6bb35ef4d1a4 | -7.68909 | -50.2924 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7eb02a92-de97-3555-9c58-3c7a59425549 | -6.01239 | -43.69923 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc1ecc71-7fc8-3dff-8e83-0fca414c1e48 | -5.19569 | -42.74679 | 2025-09-06 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86745fde-5eb4-3975-aba6-b446ec033389 | -5.37943 | -45.96042 | 2025-09-06 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af3fb45f-3879-3e74-bd3a-f46aaef5258d | -7.41935 | -44.92912 | 2025-09-06 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f219227-3362-3472-a86e-e01311a0a285 | -13.85532 | -46.26263 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8933ea6f-201f-33c2-8775-cb6ab859aab5 | -5.96573 | -53.60025 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e3ab4e0-2ac4-34ee-9148-bd6a4811553f | -8.91112 | -45.81251 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 934fc9a1-0043-33be-9cd6-6e3f4a44f46a | -14.58081 | -48.00099 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9779ae4e-d45a-3dfe-8edf-a1342ed50bdd | -12.95714 | -54.78485 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7d4f8ab-5d1c-30cc-bdfd-9bd8e6644db9 | -6.85906 | -45.58408 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 020b09a8-6d72-380f-981c-76def61b4a5d | -13.00571 | -48.05219 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d20f579-d156-3798-b558-c4fe0f2c2f85 | -7.7073 | -44.03408 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 473b622b-24fe-3b5a-acc7-e1985e0faf33 | -15.18669 | -48.04596 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e67bdab8-31e1-3026-8324-2e6b5d56599c | -9.07738 | -50.43212 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| baeadd26-822f-3cb8-83da-4a69a85c0522 | -6.03235 | -43.69569 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d56e97fe-ea6d-390a-9329-859d32e0bc73 | -14.5428 | -53.13461 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da984046-c8f6-3868-817d-8da9ccd1a37e | -6.22187 | -43.57125 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c195d37-6809-3f91-827f-e26b3a33ea54 | -7.7324 | -50.31582 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a578b3b4-17cf-39e9-9fd8-495743a6bd98 | -6.64589 | -43.41351 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7acf078d-03cb-3b20-9295-e4b2d02abdde | -6.01125 | -46.70368 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64e68f8f-ed94-30d9-9bd1-70f066c61a5f | -8.34221 | -47.48613 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24ca2586-758f-310e-8279-a259976bd6aa | -4.37913 | -48.06807 | 2025-09-06 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be35ad0b-cee5-349e-b730-76dd34cf1059 | -6.15833 | -44.20879 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea50c7c6-2727-3a78-845a-595c5229317c | -9.08597 | -47.00039 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2cdf25e-ccae-3de7-933f-59027f1e371c | -5.55739 | -46.19468 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe45da2-c51a-302a-8f8d-59b663370d02 | -7.71078 | -50.33136 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| deef9ea1-5eba-3268-a6eb-051a7d7924a4 | -4.32968 | -48.39175 | 2025-09-06 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a689747-261a-3399-bbbf-84733a6c8bb1 | -6.07208 | -43.30094 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22b2d5dd-c0de-3eaf-a61c-a1aca7b7b9e5 | -8.4907 | -45.06607 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e975c31e-0ef7-3710-9290-83f585a684bc | -7.06128 | -50.86034 | 2025-09-06 04:17:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 861fbd23-3f56-3349-9129-dc14cd40720f | -6.21842 | -43.35646 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf82c725-7d1a-33cb-b9d8-d9c50aeaeb89 | -8.49161 | -45.10385 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99f0e8f0-8ff2-36c2-aa31-71c9532e4054 | -6.05356 | -45.01429 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 337e559d-704f-3312-a8eb-5da7401d9f2b | -5.97689 | -53.59124 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f408bc1-a930-3f23-aafa-e368f78f619c | -3.23802 | -50.80475 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ddd84f-3a44-3436-b64c-8001681f78a2 | -12.95408 | -54.78363 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ade9ff3c-de36-30dc-95b1-794d1ea5ddfa | -7.76253 | -50.74245 | 2025-09-06 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6bf15990-02dc-30d0-9676-1d8c4088d5ee | -12.95816 | -54.82155 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 330f7a30-8b33-39b1-93bf-f0c21dedab0a | -6.87655 | -52.78024 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 793f5ddb-3965-3220-ad74-12be3da17540 | -5.86617 | -52.16336 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 854cebb0-0cc4-320e-8828-97e1db87bb46 | -6.16764 | -43.18844 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44929db8-7dce-3fff-b8bf-a91296bc5f2f | -8.86235 | -47.24469 | 2025-09-06 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8732bdb-db47-390a-8e77-5436e1ce1892 | -13.75155 | -46.92761 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2383b216-9072-3948-9e55-8b68b7da2ad1 | -6.38761 | -43.82682 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afb0e190-08fa-3eb0-9058-a2a5152d336d | -2.60618 | -48.13449 | 2025-09-06 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49f13232-03ce-367e-9b1e-9d24ace5e289 | -7.73155 | -50.32081 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad8be798-58cf-362b-92b3-bd50e9100934 | -14.56779 | -48.01214 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6619a99-de15-3638-9b3a-5e6436e7197b | -5.81437 | -47.78801 | 2025-09-06 04:17:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44e3bd93-f4e3-3504-9bcc-c0071a930b5a | -5.75432 | -43.12987 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4610b03-0fdb-3fa9-b118-b2b7c8c18bde | -14.57502 | -48.01315 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6d6900b-1ebb-3684-9a87-d0bf1a40bf1e | -12.9662 | -54.81077 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd447287-fc02-3259-9e7e-5c3278c53c9d | -7.00013 | -45.64658 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab4b81a7-876b-37c4-9bc6-246724bff4a8 | -5.65972 | -43.61842 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfaede77-c075-3cb6-a62f-7213f19fbc35 | -3.24221 | -50.8018 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a30418f-8b4a-3a2e-96a0-57f7d0fc67b2 | -6.49625 | -43.73989 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f49ba403-3ee1-3d4c-9fce-e01cc9adacc0 | -6.20679 | -43.36532 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6e32877-ce25-3450-ba9b-3383983a2524 | -13.00151 | -54.8102 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8356d663-41bc-3bf2-8b1a-445563c31bce | -12.63275 | -56.98775 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9423a17-a4c1-31b5-b5f7-5909ce6f70ee | -15.85291 | -52.30917 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce0fd854-053e-391d-9cd2-151c8c7a5219 | -6.60749 | -43.97775 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7030e357-ec21-373a-8dc9-7c901e3f5a1a | -9.06058 | -50.44785 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cea00360-aca1-32c6-8538-1a3cea1c9f22 | -8.36358 | -52.55943 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d5270a-bdde-3b2d-ae79-32f6df135eda | -6.9342 | -44.96927 | 2025-09-06 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eff0b95-4e44-39fc-8ea6-adb9ad4014a9 | -10.15353 | -46.22879 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d7a8998-9f3b-3b62-9905-82cd71b0bd0e | -2.55481 | -48.38927 | 2025-09-06 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab838a0d-5171-3e98-b062-1b24432b0576 | -12.91948 | -48.03251 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94024f9f-5ccb-354a-baff-b30824232585 | -15.35577 | -46.40189 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4f38ab3-2513-3c19-80a2-2732a8c8f64f | -6.20756 | -42.63282 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3476635d-6c41-341f-9783-2e863c95e2e2 | -8.93259 | -48.653 | 2025-09-06 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37908854-c653-3ae3-9b68-783ddaa45f57 | -6.61305 | -48.05625 | 2025-09-06 04:17:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 285f2979-c6d5-386c-9119-1fc51b96c881 | -13.01216 | -48.72554 | 2025-09-06 04:17:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39b57935-3070-3255-895e-4051a22f2a0a | -3.79431 | -48.87461 | 2025-09-06 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcbb3e00-8bc9-30bd-bf63-953509498783 | -9.05977 | -50.45246 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c311004-eda2-38ec-b714-101d75260bab | -6.87062 | -52.77929 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79909149-37c9-3756-a597-5be3d7781ec0 | -10.02439 | -48.34208 | 2025-09-06 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72ff5cca-7535-35bf-bc47-9490224c2e0c | -9.84078 | -48.84058 | 2025-09-06 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4c8cb0d-6d9d-38e2-a62c-9e6e7040b93b | -15.17546 | -52.40184 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3386b467-414e-3593-a683-d82a989db28c | -13.5598 | -48.11625 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6452a45-109b-3797-81ac-4c2f43c809da | -8.4941 | -45.0666 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5234b270-7d18-3bfa-a59a-fa7840063931 | -7.99243 | -45.47109 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fb75cfea-7925-3756-862b-e353db3bb70d | -6.40935 | -43.81941 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9586c48e-979d-3c1f-af6b-44bd03c039b7 | -12.95485 | -54.77982 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f75ddebf-4c03-3d6e-9e66-e56ecd6814e9 | -7.98147 | -46.34001 | 2025-09-06 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 082bdcdd-6897-3650-a19c-b7ff3fd7151c | -7.97968 | -44.5099 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fc29866-248b-3324-9bf7-f6a6332829fe | -9.34207 | -40.39094 | 2025-09-06 04:17:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01148c0f-490c-372e-825d-cf4bb220dba7 | -6.87105 | -52.77925 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3abffde-0105-318c-88d3-7cb7f13c1c12 | -6.23997 | -43.28511 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8392c10b-4fd5-36c4-9358-2c473987c04e | -8.34447 | -52.51459 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c07fc27-8315-30f4-ad54-977b509813b1 | -12.95978 | -54.8135 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5df97d47-cc89-30ce-b63d-22861e02cfe6 | -13.3271 | -51.72552 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41f8c445-9418-354a-be60-4424494e2b11 | -13.92308 | -53.99248 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 728921bf-b002-3002-a202-9b6a0fc80312 | -12.95251 | -54.7914 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e841e20-701f-3988-a152-16b4bc157f23 | -15.18612 | -47.98536 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README42.md)
