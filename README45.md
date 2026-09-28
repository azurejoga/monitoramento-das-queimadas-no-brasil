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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9752903a-f5a0-36d5-8745-729cd2dd22ed | -3.82046 | -44.09039 | 2026-09-28 05:08:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae501453-7d7f-3b09-b231-a5328848d718 | -1.48151 | -54.79477 | 2026-09-28 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e41b8360-f01e-3682-8c47-9450160289d5 | -1.93057 | -52.14019 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2da00aa6-5e33-385c-bb43-3871f36c969b | 4.30693 | -60.81929 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75cee856-b94d-353d-a706-8dd5885f8f1b | 0.69826 | -51.43488 | 2026-09-28 05:08:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5858ae6d-b99b-3a77-8de3-664d62c74b66 | 2.39414 | -50.989 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b535cfca-f122-3933-9bab-f58528df6eb5 | -3.94465 | -42.55507 | 2026-09-28 05:08:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30dc3b60-de16-36bb-a312-81b8fce8dab8 | 1.67658 | -55.94075 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87669a77-a9a8-348e-821c-09af50846c29 | 2.38239 | -51.02359 | 2026-09-28 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc434533-afa9-3d0f-bee8-3005b0e41502 | 1.65754 | -55.91676 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8315c90-ed5c-375e-9e01-d9c9d377db86 | 1.66565 | -55.91997 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea687b38-73f3-3cb1-901d-5c967a0997a5 | -2.07514 | -49.54874 | 2026-09-28 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 088da9f5-eac6-32c2-8ff8-086d55bc7988 | -3.81443 | -44.09306 | 2026-09-28 05:08:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d146501-a349-3153-b685-14a6a8194304 | 1.67076 | -55.92814 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e08406c-1049-30f2-b2c4-1a00f09110aa | 0.28684 | -50.90907 | 2026-09-28 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a42c968f-98bd-3309-8f44-9b2de0cfe310 | 1.66826 | -55.92575 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4b681c-08be-3ffe-8114-295a07f619b7 | -1.05589 | -53.58049 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3317d04-97f5-3d26-a3c6-16645bf642f9 | -3.37324 | -44.3689 | 2026-09-28 05:08:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c47db49-1d3b-3483-a98c-15c3dffd032f | -1.04754 | -53.56849 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f37d597d-9238-3051-bb1c-63c31df907d1 | -1.90481 | -52.08558 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c09208c6-2b8b-3321-b414-0097de3426ca | -3.93789 | -42.5587 | 2026-09-28 05:08:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e24d41d6-e4ec-33b9-ba45-f4f7c665d423 | -0.50229 | -49.12572 | 2026-09-28 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4767a944-ec1c-3106-8649-0fc37259aea1 | 1.65823 | -55.92112 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bbc0c24-3255-3417-a869-ef21c97f816f | 1.25039 | -51.12721 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56d61749-db42-37bb-b840-9123d869a2de | -1.05534 | -53.58396 | 2026-09-28 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39c32775-afcb-36db-84aa-9f919d35b011 | -7.70805 | -44.92958 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca0f1f7-7ac9-303b-a632-3e90ee446b57 | -11.18954 | -44.80747 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c5e514f2-a78a-30ac-bb47-7f6694811df5 | -3.01359 | -54.20676 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc51c34b-07e9-3abc-a1ee-83e73cf12209 | -3.41528 | -48.32983 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 475e61f6-853a-3deb-a793-7bf288bf5f32 | -2.90043 | -54.10653 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecda5758-5485-3b87-98ca-43ff7b5e1fec | -6.06825 | -57.81039 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e160537-29e4-3135-b126-a607f4618a5a | -8.00285 | -47.45443 | 2026-09-28 05:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86b2c1e0-bb07-37a0-bfbf-963148deb88a | -11.18479 | -44.79838 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2b0db071-b20a-3380-ae82-7d8719695e29 | -6.69022 | -45.65989 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac291e5f-e70e-37b3-bb52-f7abc84affdb | -6.69236 | -45.64504 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 144cb1b1-9bcc-32ba-94b0-9b178d7646e2 | -7.70708 | -44.93671 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05a18797-de18-3f1a-bd13-09507f6c60bb | -3.42348 | -48.33097 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ce33557-6fc1-3806-a6e1-bdf1abef43e4 | -4.98403 | -56.14693 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b98fc35f-7930-3809-b02a-f036455fe207 | -3.51542 | -50.32365 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d345626-5063-3dc9-8f59-cdf7677e03c8 | -6.09005 | -57.63298 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bfa2157-1dc4-32be-94e6-300f7aed6ab9 | -6.06228 | -57.82316 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e450e68-fe16-3e9c-8edc-98986f85fd92 | -3.41422 | -48.3369 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2096d668-725f-37d7-a638-812f692774a3 | -10.26646 | -44.61685 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1de0ae6b-1ab6-379a-99eb-8341a0d81cf2 | -8.03031 | -54.88675 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7e8e1ba8-b2b3-3187-b9d8-e710e6c12a52 | -6.7786 | -59.37589 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d27bb6ab-2457-3bd5-a5d6-e1ec4e5ed4b7 | -10.2072 | -50.00573 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c98a8c1a-718c-3c70-9daa-7e79e1fa290d | -2.91607 | -54.2022 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 53b62a60-6d39-3770-9fe1-300a806395c4 | -6.70808 | -45.60939 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b41db32d-8977-3bd2-8c2a-3ccda710a6f3 | -9.08042 | -49.87714 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bc0aea0-d93e-3373-afd9-2206b2560f31 | -8.72496 | -47.98288 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74a69bce-b40b-35db-b8b0-6cc411a795e7 | -6.07721 | -57.80258 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eab84877-6902-389e-ab0b-4066ed54ef5e | -8.22753 | -45.44185 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 379847e8-abe4-3b87-a875-dce406aeff55 | -7.88283 | -45.44594 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f39337b-9c33-307d-8cdd-367ef52299df | -6.14011 | -44.13382 | 2026-09-28 05:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 072dcf3c-5e66-38a6-bcd1-2be77dc3f433 | -7.49856 | -55.01677 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6feb413-9f85-3905-8463-cb4ecebbc3b5 | -9.1492 | -45.63157 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b552bbee-aa9c-302f-8c1d-992704f7377f | -5.72503 | -53.44979 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e21e3a-bcb1-3466-a79f-32ecc7257feb | -7.71272 | -54.77482 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e887328e-24cf-334b-97fc-d2a54175ef29 | -10.70606 | -44.43218 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26c46bd5-59b5-33da-9908-5e0345fef966 | -6.30901 | -43.60808 | 2026-09-28 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05d3d92-a5e2-3017-aca5-b5bb0465ccaa | -9.66406 | -48.9091 | 2026-09-28 05:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea070592-03c0-31e3-a70d-b7a30e009f1c | -2.67083 | -56.4557 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5b2a6c0-5800-3912-8294-f5efc68675cf | -6.83806 | -46.04404 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fcba717-d9d0-3691-8a9d-d0dee86e716f | -3.0772 | -54.37854 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b509206-4d1f-385e-90f9-0484a5a9429e | -10.10974 | -50.19432 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da90a01b-660f-3d24-8b55-0df3774ef13e | -7.32954 | -42.08267 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8734f2b0-4753-3491-b107-61e26b8f9a26 | -10.21886 | -49.98196 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42d391a8-50a7-3c0c-adaf-9da8c46ce62a | -3.23278 | -54.32015 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c51eaf9e-d768-3fb0-a3f3-572bc07ef44d | -2.78763 | -57.68789 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1496cd4-2ab2-3b07-b864-08dc84168d8a | -4.97703 | -56.14596 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d27c7b5-41c6-30db-a8e2-c044e00af173 | -8.04363 | -54.88889 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 98b92a3e-8deb-3095-b3e1-fac2008c2341 | -6.07744 | -47.29979 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9e33f070-84ca-38f4-9a66-cf3f12445e84 | -11.19384 | -44.81837 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fbfca45f-e952-3c7e-89d8-aa5316bd36e6 | -3.19089 | -51.03576 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae90fc40-0263-3240-9f01-66e16a69cf0d | -3.00858 | -54.21674 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c00c9e72-eadc-3a38-90d7-d0915c1fb064 | -8.73387 | -47.98236 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94405480-f3e5-34eb-970f-791c9c8c9dbc | -6.60152 | -47.16387 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 216d807e-cd67-348e-b767-9d678019d688 | -10.20468 | -49.99445 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46f350f9-0fea-3357-9917-82eb8dfc6b12 | -2.65792 | -51.73628 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38acd248-8dad-39fe-bf9f-085954da377c | -10.22087 | -49.99682 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c53dd6d-0528-34cb-a556-aa5efe407211 | -3.42295 | -48.33452 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2773a371-b029-3a05-abd9-d0f38e2a29f9 | -5.13111 | -50.71493 | 2026-09-28 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7aeac3ed-bf5a-3e0d-8317-7c8192cf18be | -6.59615 | -47.16809 | 2026-09-28 05:10:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4d8a368-681e-3118-832b-19a021095786 | -7.46632 | -55.00438 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f440b84-1d53-3bbe-98a4-6b3f0e36aed7 | -6.78328 | -59.37298 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 294c393e-63d4-3f92-91e8-6fc4569bee3e | -7.67782 | -54.74443 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e76688cb-4676-3ca9-bf30-b6e05375adbf | -6.70219 | -45.61767 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0eb795a-b820-3a5f-b689-1e13262708a5 | -3.003 | -54.20869 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dafa05b9-6add-3f43-b2b2-a931e1c1f444 | -2.78221 | -57.69691 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb8499dc-ec79-3327-a692-ed1769479375 | -7.27576 | -55.57973 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55356c95-188e-3fac-8146-67f41d6e9ced | -7.37976 | -42.10714 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 410ea1c7-00bf-379d-b2e2-f8485efb50fc | -9.15593 | -45.64 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b721fa-811f-31ff-ae21-ad5d877dcf43 | -7.51691 | -46.6136 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65d49e5a-9d64-326e-8405-6358cb456c15 | -8.89504 | -46.19005 | 2026-09-28 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5704bf00-3735-3802-a780-663300c1e9cc | -10.21631 | -49.99979 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 985024b4-0134-3c1c-81cc-b30a2d5179ad | -8.03586 | -54.8948 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b8860c1-2cd7-3562-93bf-e3b9159be308 | -6.78957 | -59.38524 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1df4938d-ad04-35d7-bda0-eeba9a78e42d | -8.60417 | -54.63842 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ea07e32-b82f-3600-ab7a-a2a05ed79249 | -8.95994 | -44.16496 | 2026-09-28 05:10:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77aa6b44-130a-3586-a95a-3131bab9aa23 | -9.07717 | -49.87131 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README46.md)
