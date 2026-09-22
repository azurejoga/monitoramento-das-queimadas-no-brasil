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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 270c5811-ab69-3148-ac58-d1fa1d4ec309 | -6.12275 | -57.75668 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39d46970-eede-3a0b-bb9b-4023b0fec1ad | -12.13998 | -47.39768 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cecc7c5f-5b36-3399-8d86-9895589ff879 | -6.85356 | -55.2672 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1b99a99-b5fb-361c-9c0c-979b77513429 | -3.05762 | -54.39701 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 013f5047-ace9-394c-a39d-8f93f767893e | -6.12869 | -55.81924 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e61f3527-926d-324f-a914-42ebd45d8912 | -8.18563 | -54.7268 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4854f562-84a6-32b1-89ca-b5e60a10445b | -11.31983 | -54.04015 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f8c9216f-b757-37b3-8c66-730de736afd6 | -3.05869 | -54.41288 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a33f5d8b-7ad5-3560-b8b2-03a856e7fe9b | -3.38624 | -56.942 | 2026-09-22 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f573b20-04bf-3d10-9f20-88cbc4b3e5d4 | -1.99529 | -56.54196 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfd55916-677c-3dff-95c8-4c1dd4d4aaee | -2.98724 | -60.946 | 2026-09-22 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa099a08-08a9-3472-b99e-f18a33cd0aa4 | -5.93939 | -57.69855 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68be0429-512d-3e4e-ad03-cf09bf365204 | -6.6368 | -59.92577 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a288ae88-f471-3d12-bbc6-3c84c13e212a | -6.89944 | -59.40176 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b806591-22b5-324d-8829-3107c2ed856c | -6.12717 | -59.95134 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ebc74a-1676-3d32-8f90-9c101317514b | -6.7435 | -59.41998 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b61de14-aaed-3606-a0e0-e9e6c4f4c646 | -12.86668 | -50.94776 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 360e57e0-e6bc-3cd8-95b4-6e35183ca148 | -6.11942 | -57.75615 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ace9741c-643e-392a-9f12-3487d3726dba | -10.20994 | -68.74746 | 2026-09-22 05:23:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 047eed7e-a7f7-349b-8354-05fe8b6de7ad | -11.99432 | -58.07825 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10b229fd-9d5d-3358-8251-75825e04a9cf | -1.7815 | -47.10638 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bcd20fe-96c3-3a24-8346-273527e14726 | -12.14139 | -47.38762 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d30a1bd-0ecb-318e-81b5-c7460fa7b78a | -6.68888 | -58.46331 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 442c5d45-2f3c-3f83-89cb-17f82510219d | -3.49676 | -59.19731 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9d8e31a-e6b2-39f9-b5cf-f563c38131c7 | -6.74006 | -59.41941 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0721e0e-3272-368c-8030-3fea83c4f544 | -11.04922 | -54.15016 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbcba4af-550f-3538-bf5d-3bad11d80055 | -3.46207 | -58.32484 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12f2c272-e236-34cb-9935-2f1be3dc233b | -3.90154 | -60.59303 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0f14dd9-9a61-33f3-91ec-122643c160e8 | -14.91649 | -49.89595 | 2026-09-22 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84eb0413-0deb-34a1-9a95-7c03e2ecf559 | -2.91083 | -48.90423 | 2026-09-22 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a637e928-e184-3ce8-b22b-61d72a9e6b28 | -6.14617 | -59.94625 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3963fc0-afd4-3829-b9fe-a751c181169d | -5.45967 | -60.14649 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78342102-eac1-36df-9f6d-847ff3b64c41 | -11.33209 | -51.37463 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0376ffa3-8dcc-3f87-a25d-4919284ae6f9 | -7.23556 | -55.59103 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcecb17a-2d30-3093-a894-8d482faebeff | -11.75138 | -50.81099 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d59bd92f-1d91-3be4-9d0a-e03d7e7b3422 | -8.09887 | -55.34615 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e61ce95-854e-3fa3-9947-c549c3c985b5 | -6.07223 | -57.73077 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf29645f-7441-3c8c-9639-4baa741fc307 | -3.36929 | -50.46206 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d089da0-e1bb-3955-9d95-37bef5b41342 | -9.40308 | -65.92249 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9cc8d1e-f2eb-3460-8feb-4c898190a3a7 | -4.94313 | -55.81788 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d08a236-3576-3b12-85e7-9580e4b18a9f | -7.44761 | -44.74816 | 2026-09-22 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ce16a46-0dc0-35a5-a425-f5296714e44a | -2.41019 | -58.28483 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68d24753-d84f-3c34-99a9-4e69c7498a21 | -13.51767 | -51.51045 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| df2fe540-2dbc-31d4-90e4-10494f5caebd | -3.39033 | -50.44135 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c05e3899-c1d6-3a0a-ae75-05161fa283f4 | -6.86493 | -59.92102 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a5bce5-d185-3d35-af76-22c4dee66e4c | -7.36117 | -55.43139 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 399f7118-3136-3307-be63-3f9540689e29 | -6.10274 | -57.62508 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2e90e0d-d1e8-3d08-821c-f1837d9278b7 | -1.45555 | -54.24261 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19be953a-7240-3fa1-855d-a8866450724e | -9.28145 | -46.186 | 2026-09-22 05:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5529563-8b52-387e-b9e3-9f4d1ce42cd7 | -1.29658 | -54.20781 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dd868fa6-fed3-3f94-b97b-e4493996c0f8 | -2.5723 | -57.50995 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 262ebaaa-e219-32bb-9210-ca2d909d0a3d | -6.77833 | -48.66172 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a6e269c-7411-3a3a-8c9f-698cd9aad939 | -5.91497 | -57.68036 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96885537-c6c0-3016-bc2b-50eb55e8577f | -3.75281 | -59.42154 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d81496e0-7720-3ff8-962d-ea0541c38157 | -6.92111 | -55.61187 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 829d0ec2-c3e6-3228-a7ce-0897a3cfbf11 | -2.96247 | -51.42624 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f52dede-dbe7-377c-a299-29c785c9ccc9 | -5.89616 | -52.15744 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44d954cb-6b94-3f3e-affa-3e00d2f3b31f | -7.33409 | -55.60565 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c54debc-7adf-3782-842d-e8462a35fbc8 | -3.18485 | -59.70007 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7594e239-43df-367c-819a-0efe5810f92d | -6.34349 | -57.85956 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f014cc7a-409b-37e2-98dd-00f0c2c9ae6d | -3.93591 | -59.64964 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10ec79fc-8164-3d06-b7c2-82e0bd432264 | -4.96618 | -55.82512 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dd72f17-81b1-3dc8-bc5e-d5c548f5ce86 | -7.32208 | -55.22147 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c60c1468-0adb-3e8c-9c99-0e6126a74759 | -5.97956 | -57.78399 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fc0f39-73a3-379a-8457-044e83c9829c | -3.23239 | -53.94624 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01b2b90e-90c0-3b77-b88f-95b1d80096ef | -4.53093 | -54.97292 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ea20914-4ce3-3e55-a372-812c6a591cac | -3.97131 | -59.63461 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d8fbe25-d242-3778-812b-9514f8c2a6cd | -7.57204 | -57.68078 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad3afed0-458f-32a7-90e2-8204b6411673 | -3.46049 | -58.39949 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 952ac94d-a248-30e3-b7c7-93c5ae4d0a0c | -6.52178 | -55.38056 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16805667-f96b-3a96-bc1f-d36898bb4567 | -8.35056 | -50.86905 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d489f905-74f3-30b6-952f-1823db4137dd | -6.08832 | -57.62991 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6892c8d7-f80a-3fc8-88d8-7eaee9553b75 | -12.30948 | -50.69639 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21b57210-7cae-3e4f-86c1-0e4a466d9f49 | -5.8146 | -57.73959 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09104a9f-3e92-3fc5-82cf-8c02ed12fe3d | -5.81342 | -53.51631 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f867d4-d6f6-3e0e-bc59-f99ef5d37ac3 | -5.37699 | -55.89941 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af47ebdc-3872-37cd-9b72-c60f758aabf9 | -3.38157 | -50.41176 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7b3e852-eed4-3f1f-b129-21bec5c6d4ed | -3.68128 | -60.61743 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9c9fa66-4758-3296-8b50-e0b8edceec26 | -2.96443 | -52.14373 | 2026-09-22 05:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5dc1a4-14c4-3313-aa1a-a9a6925ce564 | -5.92146 | -55.69504 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebca35b0-cc2e-3a8b-b2d5-3318c3b23f78 | -5.8069 | -52.09249 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2035aa7-6f1f-3eb7-8bc2-545f1277516c | -14.75957 | -48.44043 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff8c5ee-6f40-3fd8-aa4a-adf95c43b3cc | -12.14611 | -61.17173 | 2026-09-22 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 585e089f-3061-3a90-a171-f40ed198280d | -12.79628 | -54.04477 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c27a4f7-c635-3143-b87f-c60e17d1c231 | -2.61669 | -51.73442 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a252dc5-b800-371f-af84-c2f1dff33682 | -10.21909 | -59.40297 | 2026-09-22 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a067b83c-42df-39d8-a0d4-e36faa25d49f | -10.93219 | -58.33459 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c7b2385-6344-3c6f-9196-75bf267f1371 | -8.18534 | -54.77754 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f75234f4-585d-3b66-854e-305f4ddaadf5 | -6.09666 | -57.68467 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bfadfe0-4e94-3ea7-88b2-930e694a4e4d | -3.07432 | -61.27734 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ff9748a-8160-37ee-93ed-9a1b5d720de4 | -6.12926 | -55.81562 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 853d673a-6b74-3d54-9850-c5fff1361062 | -1.64988 | -54.91564 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c375020-0779-31da-8b30-9e35e596e363 | -2.99872 | -54.1729 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00154d43-f14b-315e-a7b7-20356b475a86 | -5.97678 | -57.77997 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7928fdab-9ae1-3d4e-ab0e-05939b9fd88e | -6.1616 | -59.94077 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3333aa5-ff95-3ed6-9c35-de393b398714 | -5.87958 | -52.12914 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24fe105b-db7c-351f-bc3c-b4fe6544ef3f | -8.7891 | -44.29213 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f4e95bfb-e0ba-3014-b15a-845e63e287cf | -3.46117 | -59.53315 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10e070b8-654a-3a8f-99ac-84808b1b18ff | -5.98345 | -57.69537 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dfef1e6-e4a8-3f1a-b9e5-d16d3751c44e | -14.75906 | -48.44484 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README77.md)
