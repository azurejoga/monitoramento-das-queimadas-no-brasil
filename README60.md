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
| ab4053bb-909d-3278-a2a2-02c66e74e84c | -12.61088 | -50.77561 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea12dbf2-73e2-32ef-9ed0-d637d717ac02 | -6.33737 | -62.69081 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bd3590f7-d781-380b-b4d5-dea4288f1178 | -10.66273 | -58.76024 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2e98357-88ab-3059-b2c9-b07f76117c91 | -11.19356 | -55.02988 | 2026-09-16 05:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf11f8fa-c549-3bfd-9bd1-ee13b2c4018d | -7.8574 | -55.45566 | 2026-09-16 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e52dfab6-8699-3f32-8ae3-baaf639f8784 | -8.63649 | -66.51997 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40ef2438-ac43-350d-bc73-9fdb89db3b6c | -9.79529 | -60.47925 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 944f85e8-ce40-362d-8045-0a4db3bd8a56 | -11.41719 | -51.42916 | 2026-09-16 05:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f49f6a26-eecc-39df-8a0e-97a7e310cda2 | -9.78804 | -60.48174 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f1dcb04-edbb-3276-99ad-ed01da0d8c84 | -6.34084 | -62.69138 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 898c2f79-c6fb-3871-b542-1b082cdd9919 | -9.0556 | -65.91493 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b31e3b7-e7ed-3460-aa90-d33a5128f546 | -11.19806 | -55.03051 | 2026-09-16 05:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15b835a0-0c80-388f-a6b4-ab53864fa69e | -6.20429 | -57.78232 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da69243-3bb0-3814-ab76-0526b7292a37 | -9.03998 | -65.92073 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7ca1a49-5a0e-394a-8fd5-af70c31ed7ed | -9.0536 | -65.91255 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ca6bf4-38d5-38ae-a54a-b17fc950f242 | -6.15339 | -57.69705 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b796f55-cfe8-3cb3-a608-5ffae0c27f21 | -9.06877 | -65.93298 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad5d6754-ef71-3b4c-ba5c-302a6aad787a | -6.43769 | -58.14193 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40ac9c03-297f-30ae-ac12-28a912326382 | -9.62698 | -61.82502 | 2026-09-16 05:36:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d358a45-76e0-302e-b619-21260a07a269 | -9.83177 | -57.70258 | 2026-09-16 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5517c860-7c44-34d4-94c6-b2b9ac6519d3 | -6.6278 | -55.12918 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d274370c-1d96-3bba-98f2-8a3a94768d15 | -8.64465 | -66.59526 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60d85838-27ce-3cce-a7d1-39a3f2964b6f | -10.95301 | -57.18847 | 2026-09-16 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e2127f-a9f0-36ad-bf3b-d779513d0b62 | -6.12889 | -59.88202 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 439f67cf-ecfd-3924-ad6d-a36a01878780 | -6.12834 | -59.88551 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d61841-c5e7-31e7-8215-20ff26724173 | -9.21972 | -60.29455 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f3250b9-78a7-3ef9-9a42-fb8e2bb2dce7 | -6.43667 | -55.60771 | 2026-09-16 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5630438-9d38-3434-9f25-72689b517749 | -11.19297 | -55.03437 | 2026-09-16 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 328c3b18-aba7-34da-bd78-1fe0a20dc0c6 | -12.63635 | -50.76939 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6464da77-0924-3a39-b5d2-dc58af05d72d | -7.86157 | -55.45623 | 2026-09-16 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3e29cd-d9ad-3b33-af7b-5bd6de93b830 | -12.327 | -57.01248 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84e15e50-6d85-3ae2-a77c-1e513f9d3c7f | -12.64354 | -50.76084 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79bfc10b-c9de-37ee-9a69-23fab76e9dbb | -10.87203 | -50.81171 | 2026-09-16 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 574a8eeb-c165-3121-8fd2-f4b4be664995 | -11.20129 | -54.12374 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7042bbf1-aec3-3b70-a654-7331079489c2 | -9.71657 | -64.9141 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9445832-6885-3cef-978a-8359a8494c11 | -7.65268 | -67.16877 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12e23281-1d0d-3fae-8449-1ec2ce03d709 | -6.3494 | -62.70448 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb474d6-93fa-3fcb-988b-64465625d9dc | -10.63046 | -61.12249 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d5aafbd-8c5f-30b2-85a5-37c9d4752ea3 | -10.90035 | -54.01333 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c961ceba-fc5c-3779-858c-c8ca68170071 | -6.69234 | -56.41116 | 2026-09-16 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d95273b-27a7-3ccc-9437-1ab600b827e8 | -7.05609 | -59.22485 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2207852d-a237-3f90-9862-0e65f561a63f | -6.02684 | -59.93066 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c3ce295-7bb0-32ae-a43c-d03c31fa16fb | -7.64389 | -67.16724 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd0ed24e-932c-3c94-a1f4-0069275c8836 | -9.04494 | -60.45529 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd16ef2a-f3e7-310f-8938-80ceb0f998b7 | -7.76603 | -61.35189 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb7c4c49-f922-3bbc-a0b0-9e5cb3d4a0cc | -6.15403 | -57.69293 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b93611e-3d3b-3949-bed9-ba7fa4466d3a | -6.33032 | -59.99932 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7938f28-36ce-37ac-ad94-3b68c7cb617c | -6.43719 | -55.60422 | 2026-09-16 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 681eb70e-0668-3c51-9b9e-77e2d70d0673 | -11.80748 | -60.46101 | 2026-09-16 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa14ce9e-e738-32a4-9981-a90fd8229653 | -6.76533 | -58.80472 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fcbd8de-bc31-35d8-a810-d84d9f27b38b | -6.12445 | -59.88849 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ff8cc4-281b-3126-a18c-dc6d5a742ad8 | -6.76476 | -58.80844 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 515f58be-1761-332a-a497-5e3d7de02a60 | -9.38904 | -60.30975 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5f26c14-227b-3aaa-ae54-cfb5a13297db | -9.13765 | -65.84047 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2ec92ee-e485-3a9b-b340-4c5726aecc14 | -9.40482 | -68.93934 | 2026-09-16 05:36:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 118b1cfd-cdc3-3a81-bd30-b793cc88787d | -7.61075 | -67.25465 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdae90a6-2630-3943-9629-9535695cdaca | -9.56374 | -59.31558 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 194f1b55-580f-3120-8ac0-ce55435152f9 | -7.80489 | -66.91645 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8baed9e-0f9c-305a-944d-380b86e4f107 | -9.70458 | -52.01986 | 2026-09-16 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19866a10-7298-3ad4-9d66-09c8b4b0fe58 | -8.6543 | -66.58913 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b730bbd-6d13-3834-a75e-f59f613d1315 | -9.06687 | -65.93065 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dd0ff8f-78a5-3359-bb5e-399b0b0c29d2 | -6.33676 | -62.69461 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36061be0-4c5f-31c9-9818-e6f94097828c | -6.92263 | -63.11031 | 2026-09-16 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e206f76-e92a-3df0-aebe-dcb4d5b04ef3 | -12.61697 | -50.77639 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f5e00595-e2e6-3a27-89c6-04a882efefa0 | -9.85321 | -48.36078 | 2026-09-16 05:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82c1933e-034b-33e4-a7ad-a52ea92b8abd | -9.05585 | -65.92342 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10b53453-e17c-3cf4-97bb-becfb3a45bb9 | -6.71033 | -58.80054 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d688a23d-d981-3c46-8063-a62f61a9288b | -10.40524 | -48.64763 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b327fb74-ed86-3043-9b48-bd5716533e4b | -10.41343 | -48.65005 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92267ed5-6ff3-3734-86d1-c944239404f0 | -9.38135 | -65.44931 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab026f1f-e86b-3bda-a4c0-7b5538cc4707 | -9.78761 | -63.93082 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9afaf09e-2567-3024-b51f-d75786550a24 | -6.34308 | -62.69955 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d546be6-e953-3e9d-94ab-523d86050180 | -9.78134 | -60.48066 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c1869a3-11df-3af6-a9bf-2485c8409a2b | -6.80922 | -58.9966 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57d88a1e-8191-3d16-a08f-e79467da0c4b | -7.65655 | -67.16743 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73681504-5170-3c1c-8f56-839e293d403a | -9.06291 | -65.92995 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17536da9-28f9-3a6f-acdf-77e9a4e1f20a | -9.88648 | -60.29947 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7070d618-c7aa-395c-98a5-d950dc25f9ac | -6.33961 | -62.69898 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b4411fa-df95-3d36-b473-080deed7de8d | -9.37603 | -58.00109 | 2026-09-16 05:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a5942cd-6899-3532-9254-14a4d7c31c96 | -7.61666 | -67.24677 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 986854c0-a163-30c9-bbe0-56cd788af949 | -9.01097 | -60.45349 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e637c80-9762-34d9-9e80-c8c812c2dd6e | -8.8309 | -62.47823 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f88f8969-0f80-3bcf-94df-d5a65fdcbf20 | -11.81086 | -60.46155 | 2026-09-16 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8088c34-584f-3c85-84ed-38ca4d98a973 | -6.77162 | -58.80952 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56dde774-6199-3850-bc22-da9e9bffc7c5 | -9.38848 | -60.31332 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e03bd93d-2d77-3bd3-b79e-922fccbcc230 | -10.89972 | -54.0146 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13390655-20d1-36e9-9460-fa590c3db558 | -8.70492 | -62.54298 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fe37314-5b1e-3c3c-99a3-4bfaf66e7e12 | -9.02455 | -61.01353 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31acac29-6dc3-3739-ae27-30d23af14d14 | -15.03191 | -48.56299 | 2026-09-16 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13e0a47d-362c-3034-a34c-c40a4b273fe9 | -13.38842 | -57.0406 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcc11b08-fbd1-3112-ab92-77bdd70cb80e | -13.75839 | -48.80989 | 2026-09-16 05:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec06738f-5d77-3cdb-a52d-603bae8354d2 | -18.03581 | -50.94448 | 2026-09-16 05:38:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 16d7e6d7-be0a-356e-bf50-1d7ee19b25e4 | -13.37471 | -57.02437 | 2026-09-16 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 643028ea-4cf7-32a9-8ba4-63580836f54f | -14.22512 | -48.51684 | 2026-09-16 05:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9157a96c-46a9-303b-927b-092abdfd949f | -15.52166 | -53.85581 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f682f1cd-c6ab-329e-9d16-b9cda79bd829 | -13.75334 | -48.79173 | 2026-09-16 05:38:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1426fd31-1534-3614-ad31-10f1dcf1ecaf | -15.03687 | -48.55992 | 2026-09-16 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fd2394c-3c4c-3c93-9b01-0df79c2b11e5 | -15.48089 | -53.79567 | 2026-09-16 05:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78686053-f9aa-3d4a-b3aa-7aff1ecaf173 | -16.75944 | -57.0934 | 2026-09-16 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e5aa2a03-356f-31c4-a799-499de9e45f9a | -18.03531 | -50.94992 | 2026-09-16 05:38:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |


[Clique aqui para ver as próximas entradas](README61.md)
