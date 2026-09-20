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
| ac701e1c-adcc-3894-a520-17a6b5803de8 | -11.45287 | -45.71975 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c7c157e-eb36-3f00-b15b-421365141c82 | -10.90714 | -53.97306 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e0f01ae-cd20-3e35-b169-4263ec7f14c1 | -10.56388 | -46.56355 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40bdd733-1328-3f49-bbef-849aa8586bdc | -5.8355 | -53.52544 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a81df27-ead2-3966-970d-8ae1f51224f8 | -12.35394 | -47.68702 | 2026-09-20 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00052992-b96a-3153-beba-da84ea279efa | -10.87327 | -54.09577 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0e6634-8291-3ff5-a1ec-653c224068a9 | -9.55791 | -46.56248 | 2026-09-20 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e9a569f-c468-38a5-874d-0814679224e6 | -9.42097 | -50.19142 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66db73c3-fc60-3e83-99ed-e993504a977f | -7.7733 | -44.83298 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2395952-946d-3db1-9943-b19e504fc335 | -9.9014 | -45.09875 | 2026-09-20 04:40:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f462c9f5-e89d-3d38-8be3-7dab34487d82 | -10.41312 | -48.33062 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e18c379-9e55-3f4f-832f-1b9683e02e13 | -11.36149 | -51.34952 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ff6cccb-b100-320a-a7a9-d172f680316c | -11.49472 | -47.78917 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31375297-d641-3fe3-aadd-0cf355a22210 | -11.48362 | -45.36607 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d31ae19a-6d3e-3f30-afdc-4aa9627eb2ae | -11.21585 | -54.07247 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2763afa1-b50b-3367-b798-f60872b8161c | -6.99235 | -45.67669 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbaea6a7-3118-3fe7-b6b4-9af82da36858 | -7.30635 | -48.71275 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 657906fb-00e9-3cbc-80ea-dc43a21619d2 | -6.38689 | -51.67755 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3e8bb12-b023-3bcd-93b9-e21fe1d76700 | -7.81593 | -45.09295 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b481ffc-b051-3edd-9d16-13dd944bce4c | -9.54294 | -46.28653 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 150fb680-0c25-37cf-b68c-37a1827de4ae | -9.25749 | -45.92472 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e4843aa-d9c1-3b17-82e1-b7df23cd1f9b | -11.88207 | -47.65702 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6aee5ee8-afc8-389c-b039-cbab482ea319 | -7.76458 | -44.84071 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d19d70b2-c592-3eb9-9c54-86e8d07603d6 | -6.87673 | -51.8738 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0154b161-acf0-3bdb-8383-2aba1bcc69a6 | -9.7805 | -45.07069 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfec03fb-407d-3b29-95ac-b06c39b1e8bd | -9.93826 | -60.72975 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d93f972-9e12-3f18-923d-a5174576251b | -10.55923 | -46.57084 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43396593-feff-3728-9610-64143cc5e5b5 | -7.07267 | -46.28503 | 2026-09-20 04:40:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 831c4509-8b0c-358e-b23c-485901baa69f | -8.45365 | -45.86399 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbcf3aba-f56d-33d9-95d3-f61a673b7f59 | -10.78178 | -46.33578 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78f04c60-de10-3d8b-a05d-b02ab3aa2f2d | -10.57557 | -46.53305 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 497500ee-765a-30d9-9775-a152cf6b84d1 | -5.84556 | -53.52239 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea2a3e5e-9771-3ba6-9447-c9b896880dd0 | -10.38486 | -48.3153 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17cb9f8d-2466-3c14-88bd-7dd0fa6ab6b1 | -10.87275 | -57.1443 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d69c2f65-c357-3e4e-ab64-b9ed3d425ad7 | -5.85495 | -53.49262 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f18382d4-a2c5-3f07-89b7-3f05b3b5149b | -11.49754 | -47.79332 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e99b13a-8197-3f40-8c38-87534417a171 | -11.22289 | -54.07906 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8039c5c9-5884-33d0-89f9-d67017e75d66 | -10.57147 | -46.53661 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed06c723-7c37-3cea-9073-f9a98d40b5fc | -11.24157 | -48.37562 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c2d3450-40e6-377c-b715-03190e29b57e | -9.57223 | -46.55217 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17c693a5-46a0-332f-bfab-9f5c4763f6e0 | -9.2404 | -45.91772 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37798cf3-0268-3d22-ac61-5b0a3ddef2d3 | -7.15982 | -47.46843 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6397282-103f-3ad7-b284-a3f2e883bd09 | -14.18613 | -47.8768 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d46b4a1-e240-3b3a-b35f-53bdfc26de4f | -11.04638 | -47.67902 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c5748b4-1ec2-3ea1-a55f-4b02d21f5f60 | -8.47612 | -44.51223 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff4bd69f-631b-3afb-85e6-d10773d8e60c | -11.19703 | -55.03954 | 2026-09-20 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae9cfd57-3aad-3005-8cfe-b45bf83ee608 | -10.27266 | -50.28241 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 929942a3-a8ba-3714-ae08-58ad7711c558 | -11.01904 | -48.30018 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d56200a-1c7c-3615-aeea-f3bd2b02be9d | -10.34173 | -45.3073 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd9af25d-747c-3330-92bd-3bb76bfe4fc0 | -10.41644 | -48.33115 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88557590-38b9-3a0a-a3e4-05265bcb7ea8 | -9.21354 | -46.21848 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e0fd935-acde-300f-9f18-03f28c467299 | -9.18567 | -60.76912 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3ef1087-50bd-317c-8966-945d1fc76c8b | -10.9848 | -46.59966 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46da0ba0-79c4-3c10-986c-2d781c2a952b | -11.47893 | -47.75679 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46650ce3-60aa-3e76-b53e-b80edbfcca12 | -9.1225 | -45.71958 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d633a0b9-c582-3646-b680-d7e45b57cbdd | -10.3887 | -51.87671 | 2026-09-20 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2be7eec7-6af6-3ab8-8889-2667618d0fbe | -9.83875 | -46.43391 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bb5e72d6-7f1a-3374-bb96-ea43e7216809 | -11.32404 | -47.34816 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 203ca097-baec-3ea2-8e24-888fbfd9c2c0 | -9.70963 | -45.99371 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7abfe217-99b7-35fc-8bb6-f3fd65c0d578 | -7.96509 | -44.0787 | 2026-09-20 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1997cd2f-2691-3d82-9ef2-a1e34ec6a73b | -10.78068 | -46.31912 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7a9dda00-41de-3c2d-85ad-8d5d2e142816 | -7.88219 | -47.64646 | 2026-09-20 04:40:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9a3543a-945e-3e08-a735-a97cf0f2e30e | -7.9711 | -44.06487 | 2026-09-20 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ee7c5ac-551d-3950-9da4-d4aecd511ad6 | -7.59129 | -46.30521 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c077bb0a-9cf8-3ed2-b25b-4bf7d0dd4569 | -9.65895 | -54.32156 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f7e8cce-413d-3a89-ae9a-29011fc0e8c5 | -5.86161 | -51.9417 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 714a82a1-8e1e-3345-92ff-4a10686c7196 | -11.02124 | -48.32974 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e33bf21-dbf2-381e-8c66-3a0026e4eda7 | -8.23009 | -45.59736 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed327ed2-e890-3aa4-bbd9-2b19929f3815 | -7.53674 | -45.42982 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| f81998ff-32fd-373d-9af5-82828186980f | -13.61651 | -46.92028 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9247c17-aecb-3b92-9d4f-30fc75158baa | -9.93202 | -60.72843 | 2026-09-20 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08077b27-51a5-384e-88ed-87369e5e2367 | -8.8435 | -44.92075 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 444c30e7-9e63-3052-9a54-4d00886041d6 | -9.79465 | -45.7206 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c750c9d-d844-3c54-9966-c0e6535d3a89 | -8.49911 | -47.43568 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 233d1f65-5971-3c08-ad05-3c1a894c131e | -11.66654 | -43.42253 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b595e7f-caa1-3284-a5be-fd6f3f3b53eb | -10.20846 | -53.92227 | 2026-09-20 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 880b9ae6-291f-37b2-8d8c-5da7370f67a5 | -10.87783 | -53.99995 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc899469-a401-3587-94ca-4c9546e66cdf | -10.40567 | -48.94046 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3478cfc-346d-39d2-b45f-c01491a72ee5 | -10.26885 | -50.26319 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c969cec5-dfcf-398d-b344-b1c73ee9bdcf | -10.32242 | -48.00084 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 690d3f7f-5dff-3105-8919-55d5f6aba7e2 | -11.48122 | -47.78709 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b68dfe0-4d3f-3ddb-b5f1-932b5ab83aa1 | -11.13311 | -54.01797 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78c0382d-c85f-37b6-901b-661855eec4bb | -7.10594 | -48.41357 | 2026-09-20 04:40:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc605f6f-b99b-3388-8421-ad156ad3a561 | -11.38402 | -51.38486 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 909a5ee7-a029-30fa-9670-4ad2f2be7e29 | -12.01188 | -44.68728 | 2026-09-20 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a82ce6b-d199-3dfa-b9f4-2685adce7290 | -9.25688 | -45.92879 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76c2659a-3c61-3225-90d8-c481ed7e1c57 | -7.52691 | -47.33495 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a47137b-c0e9-373c-9d88-efc15b8185c8 | -10.87176 | -54.08094 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cca0820-a5df-39b4-a64e-6166c017595f | -12.32312 | -50.70984 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60681763-e68f-38df-9fc9-1ac3cd7af2bb | -6.06631 | -57.73338 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b19ce45-af2e-35ed-9334-0e75cce55000 | -9.99653 | -50.28152 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 779fde3c-01de-3185-978b-b2d176cb7609 | -10.93147 | -53.95071 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 144e4afa-bede-3bfe-8908-56ea5bcfec12 | -12.75722 | -46.22117 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ff4f53f-6964-3fcd-9d96-edc259a68a91 | -5.84259 | -53.56487 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 063c7ff0-9d7a-34f1-bb10-5c89629babb4 | -9.17718 | -51.51197 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb007b6b-8e70-3f02-b14c-edbd4e170504 | -12.52716 | -50.03716 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6feeda9-d61e-32d5-b66d-f8c2a47e028b | -5.8353 | -53.5528 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64015fa6-e52c-3a98-8a98-4d888ac1e049 | -5.20597 | -56.04845 | 2026-09-20 04:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b0e8af3-0bd5-34c3-bc2a-0c30995f0fe1 | -7.01247 | -45.76329 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d06e8412-a6ac-3844-a58c-015b54099307 | -11.05938 | -49.74058 | 2026-09-20 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README61.md)
