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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4d4be24-e722-38b8-9347-c6496f171d42 | -16.01522 | -43.6031 | 2026-10-06 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0422b18-c338-36b7-a5b7-d7c7121defed | -13.02437 | -43.11868 | 2026-10-06 04:21:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b108f00-d20f-3cdf-854a-b60043ae8d90 | -11.69209 | -43.66693 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9027a232-4be7-38a9-8a7f-9c769d62fda9 | -13.00114 | -40.1431 | 2026-10-06 04:21:00 | NPP-375D | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f63ed467-ab32-366e-b39a-d4067823de4b | -11.71901 | -43.63853 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbf2f6fb-24d9-3831-9c2b-7da5089b02b9 | -11.72178 | -43.64269 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c8f7742-79fc-3935-a0bb-69232cb33b86 | -11.82206 | -44.69374 | 2026-10-06 04:21:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eff83b1-1c12-380f-a6c9-f391c05f6213 | -17.96027 | -42.41199 | 2026-10-06 04:21:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0bd228f-0199-33b3-9bf2-4f04abde3422 | -14.84761 | -42.79547 | 2026-10-06 04:21:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe94d04f-8df5-36b9-af08-98b1ac9504fc | -15.63682 | -40.99928 | 2026-10-06 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99c02221-ed60-3918-a2c1-f83020a3b059 | -14.07167 | -44.48548 | 2026-10-06 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 897b7a3d-1241-3ce7-a51f-e5660179bf0d | -12.7602 | -44.87179 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2d87c77-d7dd-3da4-8633-68533fbff9f7 | -14.80285 | -42.00771 | 2026-10-06 04:21:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff51c36e-c804-3842-8d60-d59eb69a826b | -11.36426 | -46.68091 | 2026-10-06 04:21:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a859cadb-c038-38f9-a33b-d2ff53742875 | -11.76533 | -44.92883 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c509408-feb3-34ad-b3f4-97224b92872d | -16.02303 | -45.13461 | 2026-10-06 04:21:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 568f3985-74fb-37c8-92c1-909edc149495 | -11.76726 | -44.91721 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3c143f0-ee52-3f9a-8480-e4ba9409bc59 | -13.47539 | -42.72266 | 2026-10-06 04:21:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 507dca33-a7de-3804-af74-08cda62fdac5 | -11.75011 | -44.93427 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cece485-c543-3384-b3a8-2172487e7209 | -12.76926 | -44.8812 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b55f6f6-f8f4-3933-9296-448ca20b9d0f | -15.11685 | -39.92176 | 2026-10-06 04:21:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47abd72d-cdd2-32d2-8c4c-d76d0cbd2522 | -12.20111 | -44.65794 | 2026-10-06 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0968fbf8-4439-3481-b1f2-91ddb63a6c96 | -11.53682 | -44.89184 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d775cd8-e33c-3c00-abf1-e3e412f3cf5d | -11.67324 | -43.63419 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae04a5d2-7cfc-32f8-9dfa-8e8053b3ff50 | -16.02365 | -45.13087 | 2026-10-06 04:21:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d33b91f-35cc-3dfe-a799-ddd29c1d7217 | -11.74947 | -44.93809 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 832d0601-d0d1-3a92-8120-c147e7094217 | -15.64563 | -40.98838 | 2026-10-06 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 09ac1cc3-7ff5-3fd0-86dc-61806f482a11 | -11.77361 | -44.922 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c957e3ad-0924-3a79-8fb8-984c867ccf01 | -11.69418 | -43.66393 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edb0def7-f418-336b-a1c7-4474f372061c | -12.76863 | -44.88501 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10865606-8f2b-3401-9ece-bdbc1b05004d | -11.72236 | -43.6391 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f13fe96-ff1c-3926-830b-4b8ed0ffd7ff | -11.69359 | -43.66753 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcb29aaa-8443-3c5d-b2ff-63162950d9bf | -11.36753 | -46.66185 | 2026-10-06 04:21:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cded67b3-af5c-3b67-a8d6-7ea472a39b77 | -11.6693 | -43.63723 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29e54490-c075-35a3-9c63-bfe16ba780e2 | -14.19675 | -44.36379 | 2026-10-06 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73bbd600-dcf0-3ce7-8f4f-5113968e1848 | -12.63999 | -42.85575 | 2026-10-06 04:21:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f0e2a657-e65e-3faa-a43d-6d737a431a34 | -11.68712 | -43.65498 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0119d14c-a61d-3ff1-9e51-1ffe9c9de099 | -17.71246 | -42.27687 | 2026-10-06 04:21:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10aad35a-0dd9-34b3-8665-0ece92b9eba2 | -15.71571 | -42.23828 | 2026-10-06 04:21:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94ae230c-bedc-30ef-88ed-328a8559a303 | -12.13668 | -45.10644 | 2026-10-06 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fc9bce0-570d-3cb2-a17a-39082909b5cd | -12.20048 | -44.66172 | 2026-10-06 04:21:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 671c56df-26d2-32d5-a730-f9cbec6676df | -11.36344 | -46.68565 | 2026-10-06 04:21:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27998517-09ac-336a-a451-328e8bd8abcb | -12.76112 | -44.88763 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9291909-0eee-3260-89f2-c2108bebfc8b | -11.82684 | -43.53463 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ed8d7c8-06c4-368b-9182-1f11d1228640 | -14.78096 | -44.65813 | 2026-10-06 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd82299a-94bd-3496-b485-c901ce7e799b | -11.83632 | -43.53977 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 792f730e-16bb-358b-8935-cc473410a258 | -18.53801 | -41.29781 | 2026-10-06 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c480060a-c308-3be9-b38f-b390f82c46e9 | -12.93306 | -47.4418 | 2026-10-06 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dff8aa0f-69fc-3fdc-a214-0f8a7333c1b8 | -11.82847 | -43.54579 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4c6fbd8b-bf0a-327a-93e0-8738f9f5d13b | -15.04661 | -42.03122 | 2026-10-06 04:21:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17fd1128-4b19-327b-bfd6-591d51bb5607 | -12.75894 | -44.87941 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df1c2bfc-efdc-38c5-99cb-1fdabf0f3281 | -16.04031 | -45.11459 | 2026-10-06 04:21:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3dd9f0b-db32-3441-bf6e-e2e3838eb9bd | -13.87687 | -43.79406 | 2026-10-06 04:21:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dcdd6870-1ca9-35eb-96ee-25f63d9ed373 | -14.78157 | -44.65445 | 2026-10-06 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bec2cc21-b123-30da-9c28-a1a5aa8658a9 | -11.83575 | -43.5433 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37f50598-5f39-3a3e-9a6c-457d29590311 | -11.71842 | -43.64213 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 122ab419-90ee-3762-a7c6-f8d802260330 | -13.61372 | -44.35641 | 2026-10-06 04:21:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7752a568-8246-330d-8d7e-d6027855bc96 | -17.76336 | -42.42563 | 2026-10-06 04:21:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cff6ada1-70bb-3fa3-9b3f-7a6a6cc34194 | -11.693 | -43.67112 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac1160f1-d11b-3412-bee9-fdee5e0bf6cc | -11.76312 | -44.92059 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ef1404b-9324-38c8-80e7-6b20afa59a3c | -11.69241 | -43.67472 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a269c10-455a-369f-9e41-c99cb9fa3105 | -11.53617 | -44.89572 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99b3d939-818e-30d4-8720-dfde7121d670 | -16.01246 | -43.59893 | 2026-10-06 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 29b0608f-4a23-33c4-a608-ea17e8df92de | -13.73486 | -48.48225 | 2026-10-06 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72730f31-0ef0-367d-9675-02c6338539f0 | -13.14693 | -42.55994 | 2026-10-06 04:21:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed75b029-964f-384c-84aa-fecad3421816 | -18.03653 | -41.66663 | 2026-10-06 04:21:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd5fc722-ae35-3492-9989-86814dd6266f | -11.68506 | -43.62503 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f13612a7-ed18-3254-b85c-e5c48d73dd8c | -11.69183 | -43.67832 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 074141a5-8476-3c80-b01b-eb9f998beec2 | -12.76238 | -44.88 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04da3ac5-d1de-3ac6-8ae4-06fab0c2f17c | -11.68771 | -43.65135 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98ffc2fd-23a0-3545-8d16-f7b6ef212117 | -12.21509 | -44.27702 | 2026-10-06 04:21:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bce56cc9-af14-3c47-9783-c88de7a383d0 | -12.9991 | -40.14443 | 2026-10-06 04:21:00 | NPP-375D | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 195ffac6-3a9e-39ce-87af-518e0b115843 | -18.536 | -41.29911 | 2026-10-06 04:21:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b7f60991-cc36-3e21-a785-28bbe118054f | -11.69577 | -43.67529 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d60369e-36c9-3843-ac83-f53d8b8b0391 | -14.05083 | -44.29104 | 2026-10-06 04:21:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c1d9773-d21f-31d7-9a0b-749bf3924cbd | -14.79861 | -44.35303 | 2026-10-06 04:21:00 | NPP-375D | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e4dad8-fea4-3f85-b6ff-028d636a3180 | -13.50596 | -42.7021 | 2026-10-06 04:21:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7e3973b8-4a03-38f7-b4d1-946ce9e7082b | -14.08211 | -44.01348 | 2026-10-06 04:21:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 18cde168-35e4-35c1-ae8d-4162f89c08e8 | -14.78063 | -44.65472 | 2026-10-06 04:21:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2343944-0e4b-3fef-aa63-29c3ae3c745f | -11.82613 | -44.69051 | 2026-10-06 04:21:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52e25cc2-6a8b-33a0-85da-a95c2a134819 | -12.76364 | -44.87239 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07edc79d-2b84-3134-93f7-b66a6f8f01de | -16.03969 | -45.11832 | 2026-10-06 04:21:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbeeeef0-6d13-384b-acfd-9d996ef24446 | -12.63943 | -42.85929 | 2026-10-06 04:21:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b42dfb80-1fc0-3553-b2f4-5b7e621be954 | -16.02704 | -45.13147 | 2026-10-06 04:21:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cd32e6c-ec21-3e0b-97c3-a9a2c7a91d3d | -15.52782 | -42.63867 | 2026-10-06 04:21:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 07af3e9d-c7de-34c8-a5e1-a4541a7e54e4 | -11.69519 | -43.67888 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d78e8d93-adf8-37e9-a983-c39c998ea7e9 | -13.49389 | -44.36151 | 2026-10-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17f17b8-086d-310b-9876-87bb46164e7f | -11.71399 | -43.42418 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0103334-1ea0-3d61-89f1-4526d3bfb9fc | -14.75935 | -45.14615 | 2026-10-06 04:21:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 074b7b1f-a6a9-3546-9057-e26aa34ffe8f | -11.6775 | -43.67185 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e369af4-7388-3165-80c5-2b0826d8afb1 | -18.54159 | -41.29836 | 2026-10-06 04:21:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 423b029e-bcc1-3151-9153-38d91f8a1720 | -12.76301 | -44.87619 | 2026-10-06 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03a30cca-6b8d-350f-9738-ff22f7d1bdd3 | -14.76277 | -45.14674 | 2026-10-06 04:21:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 07a0cf71-f059-3949-92c7-80e73b89c9a9 | -11.82348 | -43.53409 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f9ded22-c93d-36d5-8208-dcc7c2fa0495 | -11.69636 | -43.67169 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80e6506a-7722-35fb-890a-35e478489a54 | -13.5815 | -44.42604 | 2026-10-06 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6c6e0ca-517a-319a-8b6d-dd397e66489d | -11.53268 | -44.89514 | 2026-10-06 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c9f563-cafc-3835-8900-661ef6608ccd | -12.32496 | -47.83999 | 2026-10-06 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e94e1dac-405f-3d78-b194-177c43b9eb77 | -11.69267 | -43.66333 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 121f2261-f31c-32b6-979c-bfe6aed40eb3 | -11.68841 | -43.6256 | 2026-10-06 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README35.md)
