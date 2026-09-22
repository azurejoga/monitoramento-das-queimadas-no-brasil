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
| 34b22821-2913-39fd-a364-c33d76579d1a | -2.65785 | -57.7818 | 2026-09-22 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d9585d5-5d5f-3b41-92e5-29f6c9d72a14 | -6.09831 | -57.6315 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a2b8cf8-a8ed-3919-8d2c-358494c5629b | -3.47824 | -59.57618 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5d46008-f3a2-3a94-b4f7-2d334179360c | -6.35589 | -55.83895 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6eeb094-90b3-3eb4-bc2f-60fa899e70b1 | -14.7521 | -48.43343 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 577e4ff3-e0d8-38bb-b881-3b1835fe6a1a | -13.51183 | -51.52288 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 77da5682-16f7-347f-bbe8-2b190a1bf5ea | -7.32353 | -46.76496 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6cbd887-7488-3e00-8295-2b4534637d00 | -3.2036 | -57.84192 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d740e23e-23ae-3597-ad3c-82e563dce37e | -12.95682 | -50.98233 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54a844cd-7878-3de7-b97f-04b95eb353cd | -2.3124 | -50.45137 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 930a7c60-3d1d-30ce-b3f8-5202e007501e | -6.01442 | -47.90363 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6710746a-ca4d-342c-9d37-5184f78045fe | -5.90669 | -51.77454 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7edd808-f2fc-35d0-9685-ea7be24513bc | -7.59365 | -57.67352 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16f0c869-17c9-3545-8fcd-25c9f4b9e90d | -3.89852 | -60.58793 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c22c40d4-02d5-3312-91ff-3b7ae0f1d2d9 | -6.46723 | -59.99226 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f335de5e-9058-3f7b-9247-0206188bb3c4 | -4.1853 | -49.4061 | 2026-09-22 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ee9a281-8e2f-329e-9550-94ccabd68f8f | -6.16363 | -57.79526 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69ac30ed-9bdd-3020-8a7a-5c59123b6247 | -3.17065 | -58.5967 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19a3e344-d822-3e77-ac96-5d968ca901d1 | -12.95543 | -50.93262 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b7323e0-e835-3ab1-ac87-03008b1c97d3 | -11.03831 | -54.14368 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf9136e-e00e-3201-80e5-3746d8dd6900 | -3.80626 | -58.44174 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50d37d5-f379-3e19-9311-d4010f1b8873 | -3.17754 | -58.5978 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a0fc77-3833-3bb7-aaa9-45d896477490 | -12.88276 | -50.93872 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 113b610e-90f7-3659-a251-012c9c56781c | -3.55647 | -50.28819 | 2026-09-22 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33eb290d-02fb-316c-be44-875f6214992d | -7.59255 | -57.68048 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 11c534f1-aece-3ec3-9d83-41a5495aacc3 | -10.91547 | -53.94233 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9eecf2ba-8a71-3e93-b34c-0c0bdd71c044 | -6.13895 | -59.88012 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2346acc4-0faf-3e14-b9bc-4f1e69e11e8e | -14.04958 | -52.05239 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2846d837-fc46-3b8f-9452-8a4de270456e | -3.77097 | -61.19624 | 2026-09-22 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03cc4b4-ad0c-3785-ac26-f6be811d78c0 | -4.93976 | -55.81736 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a1a00d-ddd1-3f93-ad72-d498de032859 | -10.90396 | -54.07566 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79d9b9f3-dd3f-3f49-be92-3ccb60b51905 | -2.72728 | -51.55507 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0264d6e7-39ec-368b-b3d7-e6f0ebf5f42c | -3.68791 | -60.57672 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37347c77-82e9-3f7d-821c-9aed2b76352c | -3.46474 | -59.53371 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba17cb62-fa2a-35fd-9b7b-3397f563867b | -2.78857 | -59.89043 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ce93169-3f66-3eaf-91d5-a69357a82ce1 | -6.30855 | -60.01683 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f94c7ad-b883-3d1c-b841-c00c975bf7db | -2.62147 | -51.72991 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de0a8bd2-d44e-3e62-afd9-9499b0bcf107 | -5.86956 | -51.94136 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4112dcfb-974d-3292-a95a-2acd3531611e | -4.66397 | -56.03202 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 952e26e1-03f8-3239-a251-c9264f4bf77a | -9.6071 | -43.92953 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e306408-48d1-37e5-b220-f85eb28b43aa | -7.08178 | -61.08305 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebfeb413-b699-3344-8857-0971932eaab2 | -3.17125 | -58.59297 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d2b51a-2092-335a-98c3-d50dca8a8f6c | -3.40557 | -59.58228 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c5e0893-1ca8-31f0-8c26-b45a4ab5ec68 | -3.39592 | -61.06626 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eee4a7ea-bc65-3c5c-90fd-02d0ce337ae0 | -3.06793 | -61.29184 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 921d5e5e-ba35-3ac7-a393-ca2b10ac4e1a | -2.88785 | -54.07732 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc3a5e42-9913-399e-9353-a9b972f07aad | -3.07198 | -61.26659 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1e00535-3da1-335e-b400-82123f5e9808 | -3.89477 | -60.58732 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e21ee17-2a6c-3f2a-83be-c24c89f8ce85 | -4.09207 | -62.09209 | 2026-09-22 05:23:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd0f9113-1210-3688-8dd0-639d912434fe | -5.9244 | -57.68542 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89639add-fc79-3c37-9c3d-0af22e3d21f8 | -3.06564 | -54.41395 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7beb42fa-0bcf-3d60-9b92-14ccadd2b675 | -6.29019 | -57.74384 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f89a2be-5832-32a9-ae3e-608aa01b6e53 | -7.58923 | -57.70137 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a48d5baa-ec43-3a56-a14c-f457d182f154 | -4.52907 | -54.97575 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60bc54f5-0622-31c3-8d4c-903af7579dd3 | -6.15305 | -57.84005 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f81f79f-782b-341a-8c40-5f0095bda644 | -3.00512 | -54.17787 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 123dd364-c8e0-3fbe-ba61-9190bde91fa3 | -6.01129 | -45.24438 | 2026-09-22 05:23:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 085a0a5d-bb75-333f-a845-f97b0af49b00 | -6.85645 | -55.27155 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83e68bf4-b3b2-39fa-a53c-1c2995c07018 | -11.68913 | -50.98676 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 8810a17d-1725-3971-bf8b-d4da9e0b8e6a | -6.10387 | -57.70366 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af98570b-859a-3e71-8042-8177bd59d197 | -14.68089 | -45.67795 | 2026-09-22 05:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdc33cff-2a92-348b-b26f-1e53ad7ef6e8 | -6.79035 | -55.82668 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b508990f-6346-34ba-a3c7-25dd07a7b121 | -5.82734 | -52.20145 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0dc253f-d98a-3958-af6c-eecb29820500 | -7.609 | -55.34245 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5978994-80d0-32a3-9f6b-bdc8edab6058 | -13.86921 | -48.57098 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e13f5bb-a836-38ed-a75b-2129ed054f1c | -7.35557 | -45.34644 | 2026-09-22 05:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4f2c1c51-1114-38ea-b444-ed77ce9a9c2f | -14.7538 | -48.43842 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 975b179e-89e3-30da-8a14-9aaea72c9363 | -13.51699 | -51.51561 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 4bb6d6d5-facb-3ffe-944e-912377760fe0 | -6.55561 | -56.03595 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c4cf37a-4beb-3755-aa3e-d434137d6a73 | -7.62023 | -57.6135 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a31c2c0-1643-33b2-b8ea-04a831975890 | -6.09553 | -57.62749 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63388baf-2b60-3fa1-af83-63af4fbadc43 | -2.95493 | -57.71867 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45469cd8-78da-3be0-a9c6-a75d3bc7d4fe | -1.93725 | -56.60715 | 2026-09-22 05:23:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4c81e5b-501c-3152-bbf9-89d551b89268 | -13.87544 | -48.56696 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cba26918-eb1e-3aec-9d05-6ae6bc81129c | -6.65458 | -50.9333 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0c60d78-44c1-3d0b-98f4-449cfc7b5904 | -8.23232 | -54.68707 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c45419df-3d78-36fe-9d9c-8be5e9ae463d | -3.91196 | -59.6168 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2f670b5-32a7-3ceb-8089-82ae9d8db520 | -6.46305 | -59.9956 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b69a4374-7fdb-3092-944d-35943433f19d | -2.86862 | -57.79628 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 950f0b84-b7e3-35f4-b252-35842740a665 | -6.28333 | -56.03521 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c084707-8742-32dd-adbd-0e04bf5c3500 | -7.82877 | -45.25618 | 2026-09-22 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fcd2ead-4ed6-3b9c-bbb7-7bd746f08424 | -3.68661 | -60.63227 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c210d004-9633-3968-a8c9-55113295d2a8 | -6.0051 | -57.70953 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 884fe925-2164-3397-92e5-dda25f17a446 | -5.99776 | -44.72663 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36b424d8-324d-30ea-8378-b36eba41bac3 | -3.3079 | -57.86533 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6bbc295-eed6-39ea-9abc-2a6bcbf3f980 | -6.78313 | -48.66568 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09238a59-67b7-35f7-ac8c-411baf2dd025 | -5.75601 | -45.083 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5ef38b0b-5342-3da4-9a89-51dc1df65fc3 | -4.10291 | -56.34555 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a54852ad-c88e-3e75-a3c3-c667d715290e | -5.969 | -57.7859 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86fd1c21-3c55-3264-b062-807bd473f4af | -2.91638 | -54.19282 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5d37cd1-a41a-3c54-b5cd-8416424ea062 | -5.12805 | -60.28016 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4b491c1-37ad-37b5-aaaa-e746fbd48596 | -2.41882 | -58.27487 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f441d8a1-477d-3742-ba58-70871fadc126 | -5.20858 | -56.09861 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 955d6fd0-c955-3b62-b1f6-f37ae6a8dbb2 | -6.6205 | -59.91501 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 33b3ea44-5a8f-3268-aaac-1daae9e1a924 | -7.57038 | -57.69123 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91a7be8d-863b-3786-a0e7-1485877f6e11 | -3.49321 | -59.57443 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf5f6e84-a734-3e0b-b8d3-0c9d49de4973 | -3.20919 | -53.95524 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f67c2fb0-d041-39f0-a86c-8a253e62976d | 0.01015 | -60.60537 | 2026-09-22 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 384310eb-a3d6-3f33-a48d-6a1aa97fb939 | -3.79599 | -59.70734 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a0ff6a5-332d-3b20-b943-e3812323c588 | -3.26142 | -54.27084 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README97.md)
