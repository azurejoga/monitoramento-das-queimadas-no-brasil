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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d3270f-4e3e-329d-b3be-5e90640dface | -9.9124 | -46.56753 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd5c5141-2c03-3573-ba2a-126dfb410d3e | -11.19901 | -55.03069 | 2026-09-18 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87077aea-77a8-3cc3-8bce-f68dc64def87 | -8.28871 | -45.6245 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa3fb057-1ccd-39d6-a1bc-71638623e8d4 | -13.74254 | -48.80685 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bd39825-6768-3bec-b010-705d264af77c | -9.91859 | -46.52855 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad96ad10-3a63-3b79-a216-4f383875cd5e | -9.94093 | -45.32208 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a22361b4-14ef-3496-bccf-c7ff5496b039 | -12.65731 | -54.71661 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4671d2d6-d7ff-39f0-8280-5fda0b306549 | -11.31366 | -47.25443 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 938a7cf7-5aa7-3aa5-a911-c294440d82f2 | -14.80219 | -48.56068 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2fc45f7-c077-3c2e-a54e-6cd29833e1de | -9.78705 | -46.09018 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30b74e7f-0dd5-3387-a3be-ceef4bc5ac65 | -15.08789 | -48.72573 | 2026-09-18 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ce29e54-0232-3059-a3b6-1309596712c4 | -10.12401 | -45.56938 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| befebe16-98ab-359c-9de3-479b8fb66a81 | -9.71643 | -54.82057 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 931146ef-8b4c-3e6e-97d3-0805edb2163b | -8.45924 | -44.5046 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 656913e2-202a-3a12-ae61-b26c0c335252 | -13.61678 | -46.96032 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e02e3ad7-7e24-33ea-8589-06a6af04b18f | -9.84093 | -48.38112 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 245c856d-f6d7-3aef-a349-f37c517fe07d | -8.88577 | -45.89497 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b62b1aef-0878-31c7-a218-f31844d22965 | -11.81031 | -46.80819 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e132359-6f29-3274-b72c-cf178de9af7e | -12.28986 | -50.75519 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf985092-1bf9-31d9-840b-ead592a51ed9 | -11.66883 | -54.44675 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 35756e66-c868-3133-b8b1-83cbc016a071 | -10.50931 | -46.27845 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16be9828-b645-3590-8e44-b00097c290ea | -11.29348 | -43.39556 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20adecf6-7f42-3462-9629-f53818569a45 | -8.47997 | -57.6263 | 2026-09-18 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d6ce623-2c7d-3d85-8160-719d4c4f61be | -9.79312 | -46.09473 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29a83b75-aff9-3991-bafe-f7bb5e130999 | -14.39257 | -47.26041 | 2026-09-18 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee91605-7bc5-3d69-8a1a-4eeb3e02dde7 | -12.56254 | -50.74507 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62fcba76-471f-35fb-b3bf-aa2d3318bb90 | -12.55955 | -50.73947 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f99b66a8-7940-33be-afc6-bccc345ee43a | -10.67073 | -50.27616 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac1b6712-2794-34c4-994e-17b31e0d9c6e | -11.9917 | -52.46309 | 2026-09-18 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7607b32-db3b-3047-aa77-32ebb0249255 | -9.58206 | -46.56852 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e13480a-7edf-3dab-8b4c-af05ae82382c | -9.7241 | -54.80849 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d322a492-fd62-3240-8418-b402b76994b0 | -11.17133 | -42.8515 | 2026-09-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd72c936-71ac-336a-893e-897bbdf00b12 | -12.62966 | -50.89301 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2877e1ce-6d26-33b2-97cc-bf5a2ce68fd5 | -8.4397 | -45.78744 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5221d441-49b7-3a1b-8bf2-ce4e3718279b | -11.67381 | -54.44769 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ca6b87-da10-31dd-862b-11850b23ba35 | -12.29846 | -50.7516 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b076684-6876-329a-bfa3-15cb04649933 | -10.20477 | -43.19953 | 2026-09-18 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5658e9e0-e035-36d9-af27-dd6800afff53 | -9.76114 | -46.08245 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53924e7b-aa9d-3fd3-9221-97dd0fab6d86 | -10.67157 | -50.27129 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9b5f2d3-58b5-3f2f-97bd-225b0b3c5702 | -11.89887 | -47.5708 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae7ca8a0-40e5-3004-9945-fe6f4795ed68 | -8.44619 | -45.70285 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 207db860-05bf-3b87-90d6-9c18f932a6b6 | -12.44712 | -55.00334 | 2026-09-18 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e5c14e-93bb-3312-a2e6-3850d164c265 | -9.73853 | -46.11827 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dc9182e-c2ca-32f0-879f-81ad71d87116 | -13.36245 | -46.30261 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 456b6564-4821-37ae-890c-12278bded0bb | -8.84789 | -45.91769 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4048c01d-8dd2-3982-bb3d-c14d802065e8 | -10.66194 | -50.48883 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1b86447-8363-3ab9-bd9e-23eabd1225e6 | -9.94188 | -45.34013 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c864660-3798-3b53-8428-e32b5b589e62 | -9.15792 | -49.98953 | 2026-09-18 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aa7afe0-0395-3d43-a180-46267117e59d | -8.44066 | -45.69489 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed3a6d31-8e59-3e3e-8030-b7f98862e7ca | -8.77697 | -46.90178 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1208ab2e-d03c-33c9-86db-1e5b978459a8 | -10.79558 | -43.75104 | 2026-09-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cf8977e-7fb1-3ecf-9214-aed84a714042 | -10.6654 | -50.46875 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 96b0db75-ad27-3ecd-85ec-7caf5a02848a | -8.89663 | -44.97398 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 541cc131-22b6-3bb3-b02a-d97fc10dcf48 | -9.83152 | -49.234 | 2026-09-18 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49152897-e788-3a97-a6d5-c979c8cfbe16 | -9.1893 | -46.74625 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7481183d-1188-389f-b0b4-ddcbd028af02 | -8.77814 | -46.8945 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d9ab79e-be48-3b8d-a48f-bfc779fd0721 | -13.61698 | -48.30727 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66cb7950-ab54-33aa-9332-fff56f9a8b4c | -8.91181 | -45.00917 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44e28916-0c7f-324a-97d1-9f5391edaf43 | -11.53646 | -46.88306 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be727444-41ec-3da4-9a06-82b4eb7d5037 | -10.31936 | -45.33915 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb071995-61e9-3e62-915d-eb7d6ed962fc | -12.53214 | -47.08339 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 323cfd41-acdf-3891-9bb5-c6b4af2661c1 | -12.55529 | -50.71849 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 521f6c69-8a7c-310d-9139-01ec9a4701f3 | -9.60419 | -45.32222 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96c6694a-e061-3c85-a827-dc5e1dd58879 | -10.48765 | -45.28307 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a536e4c-3762-3d9d-af56-b776c82bf009 | -12.97834 | -46.9312 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6e5d883-689a-375c-8965-fea87f03f458 | -11.32065 | -46.76368 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0d145d8-8660-39be-a88b-208578d4c6f8 | -10.29891 | -45.31802 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 200bdf99-faf8-3f46-8508-c632897421a2 | -13.68492 | -48.59852 | 2026-09-18 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1aa3023b-6558-3ab5-94ea-9a2d22660a11 | -12.38537 | -50.69379 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9217888-9baf-3c00-b3f7-d15559e899dd | -8.93731 | -44.40154 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82c4fe34-22a4-3418-9fbb-9faa0ceb9be1 | -11.36184 | -43.94681 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3efffb5-2116-37ab-8bfa-66bb06314437 | -11.32784 | -46.76127 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0135dfd8-826b-3532-92fa-bb93e2e0b79e | -9.78098 | -45.0386 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fb0fc6a-d3cd-3ff2-92f3-d30a7c2451e7 | -12.32608 | -50.75958 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bae937d-c810-3716-bef3-7ed6588f6bae | -12.61889 | -50.88593 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d49b6a1b-9d67-3df3-a6ba-5eef5e98837d | -11.33667 | -44.02118 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32ab4be1-9277-342f-95ed-8d19e2c0b7b5 | -12.67626 | -43.91158 | 2026-09-18 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 206d9fcf-fae8-3270-8ffa-e7a058a75387 | -11.80142 | -58.17562 | 2026-09-18 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb087ed0-5dbd-37aa-b437-52ffcd210075 | -11.81919 | -46.79513 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88427ccc-c8b4-3e8a-a0e3-4487afc37a53 | -11.25511 | -41.90713 | 2026-09-18 04:21:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c141385e-45a8-3c24-aed5-69493437e551 | -13.62618 | -46.94375 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f48aa10-4438-3a81-8c28-fa3ced5b51a5 | -10.01883 | -45.49868 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a96b37e1-01fc-3cf6-9560-5e5a4cf31034 | -11.47737 | -45.72089 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c5d86d-ef03-3721-b076-5c636763e857 | -12.32001 | -50.76566 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 013a8986-1505-32bf-950d-88a87d01da9e | -14.8062 | -48.55754 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fce7dff7-c239-3ebd-aed5-51f59d8aa866 | -11.29875 | -43.38422 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c44874ca-f0ff-3d43-b890-cd982329231d | -9.57873 | -46.56799 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f6a2e99-6a0d-34eb-bc05-d5e2dfd9dd67 | -9.95562 | -46.59622 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0786af0-9f96-3d4b-9d2e-b4bf2a676bb9 | -9.9523 | -46.59568 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 401d66b9-3fbb-37b1-be1c-31700e2db64e | -9.65211 | -45.91075 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34ba68ed-7907-3026-a76a-09012d11031a | -13.74919 | -48.803 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e79763ae-24f2-33c1-9b24-d52d69ddc825 | -13.64495 | -46.93232 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9be2a6b-8ca1-3671-be60-a23ef1c44357 | -9.17809 | -46.75182 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa93aff5-f76c-3d07-8e64-e6f141065f75 | -9.94395 | -46.60533 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86332494-321e-3813-8e55-8528dbd871d9 | -12.29071 | -50.75023 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27b6bdba-f600-3b83-a859-3c5d1243bb47 | -12.33296 | -50.76591 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bffe00fa-6457-3840-8498-520e2ffa431a | -8.85014 | -46.97326 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7798ff9a-8e41-36a9-919a-f6db8626b43f | -12.16981 | -46.98711 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d8825d34-1708-348e-aa31-65873c5bbbf2 | -9.76263 | -45.0466 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12247426-03c4-31fd-a65b-2f39b01d1c56 | -10.4033 | -46.62564 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README43.md)
