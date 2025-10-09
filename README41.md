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
| b678ce0c-a49d-3cb2-a563-675640386a4e | -7.59275 | -44.03585 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e4eb4f-3a54-3b54-8d68-d2935d6bb417 | -11.86075 | -44.92318 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ba5a9a-0602-3cb0-96eb-883411cea83c | -9.98012 | -43.599 | 2025-10-09 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b09d575b-73fb-359d-98d3-0086e307decb | -10.19357 | -44.5553 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 552fdfd8-97d5-3bfd-9fed-a7b95c339cd5 | -13.27097 | -42.50266 | 2025-10-09 04:19:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4a939a9-b75d-3bcf-857d-6dd0fed9b3a6 | -13.6783 | -48.75144 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98f1c739-eefe-36b0-96ba-a144a3b12230 | -7.99816 | -44.46059 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e86b5e88-3203-3e99-bb7e-fc80441b1860 | -11.87279 | -45.50108 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19ef876b-bb49-3e66-8d89-5cee5785b44d | -11.78986 | -45.14151 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc879699-1754-3fc0-a67d-77f689936d9a | -8.4319 | -47.19695 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9d454de-b572-3a48-989e-48a528c67c76 | -7.7956 | -42.61331 | 2025-10-09 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fd270bf0-3cc2-329b-bde2-6ff42dabfb40 | -13.2504 | -46.47694 | 2025-10-09 04:19:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bee1552-1305-3feb-8a05-c800934cdcfd | -9.05716 | -41.73516 | 2025-10-09 04:19:00 | NOAA-20 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6d1ea32-04ca-3dcc-9ecc-9fc67df923f0 | -12.42797 | -45.70607 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ccd7f703-6502-3e76-9f43-ccddc04afc2c | -7.75993 | -44.02941 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dee305fd-118e-3de6-893c-5ad4d8a12d4a | -12.17277 | -45.03488 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eff2770-393e-3c7d-aff7-d6cbaa7d97c1 | -14.78247 | -46.1078 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6345f4f-0e28-317f-852b-2dfbf327dc97 | -7.56397 | -44.95259 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eb108b0-4d2f-3058-bc48-29da13b893df | -12.25666 | -47.88388 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 648bfc95-b262-319a-8cc0-867e8f0b96f5 | -9.29959 | -40.23623 | 2025-10-09 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04fde402-6eaf-3e77-b78c-9d81bd023f56 | -7.76271 | -44.03343 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c393135-5559-3b6a-b483-12898852ebb5 | -7.8265 | -45.1835 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 397ca522-98b3-3f0a-9400-3fae9651ca0a | -3.56873 | -43.51142 | 2025-10-09 04:19:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7135f7d-8718-3807-9dcb-f58024cc1183 | -11.86742 | -44.92419 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d4ca526-1eea-390a-b642-aa393e2496eb | -8.60768 | -45.0981 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4be3283f-a3ce-389b-8571-a679d93ecb2b | -10.44603 | -46.63303 | 2025-10-09 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eb0b4b6c-99eb-3982-8534-4fbc829bd763 | -12.23329 | -43.78323 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 455337bf-1da7-31f1-bc9c-e0bf4305a85f | -13.82594 | -45.79857 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e8b48db-89e2-3031-ba69-94e0f20c8204 | -8.53063 | -46.20073 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d9febdf-6937-33c6-b78c-f66a1b5c5a45 | -7.9943 | -44.46354 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97510f13-971d-3d6d-a95d-d0f3e8c812de | -8.61539 | -45.09221 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c758c5-2f5f-35b4-b90a-592c6ecfa208 | -13.78219 | -44.34949 | 2025-10-09 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d38d21d-1daf-34df-8584-2266a5543bbb | -11.7777 | -45.15403 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d086abb-848f-363a-927e-7d8b28425d62 | -7.81369 | -46.7088 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a3ed7d1-a389-35ef-a751-b96a4750db28 | -7.65468 | -43.89729 | 2025-10-09 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6f8a3bd-9ef1-3737-af23-443aa876d268 | -11.46739 | -43.48209 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95dfc604-f880-364a-b45b-44c9f873fb2f | -7.76549 | -44.03745 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e53d2b9-50e1-31f1-a768-f52e2e2fe3f2 | -13.3917 | -42.69747 | 2025-10-09 04:19:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67e452cd-9fb9-308d-a80c-dbd0ad0d13bd | -7.7982 | -42.40919 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bfbb01d-5b2e-3f32-b009-9958aeec8606 | -11.87666 | -45.54133 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 373c0edc-8e05-31b6-a212-6d722db1c147 | -7.69185 | -42.97097 | 2025-10-09 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4df283c3-da11-3a51-a0fd-ab5a9d49b90c | -14.42017 | -43.9866 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d751b479-c1b0-388d-bb06-29a9d17b11be | -9.769 | -47.70727 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c6e686f-0422-31af-b914-3bec0a2aaade | -13.33057 | -40.90192 | 2025-10-09 04:19:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad055c50-34ae-3670-99ae-f89f532e2fb3 | -13.82704 | -45.8133 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e78dd154-a243-3fcb-ae60-88b7c80bcb2d | -7.7566 | -44.02888 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4dd845c3-2d81-30b2-8163-3e5fdee0af2e | -13.80549 | -45.84252 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0c3dd8b-c6de-399f-9903-370b1b193bc9 | -13.82043 | -45.79038 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39b3ec62-dd3d-349e-b470-eebbf9ae7a18 | -13.14407 | -50.00208 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8825a99e-2b0e-37ab-9478-198e6d8fb04b | -9.75985 | -47.69777 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b741e28-1b92-3dbb-9d03-f609860321be | -10.3569 | -50.286 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c5abf05-e922-3a58-a107-a4ebf1bae171 | -10.83257 | -49.38933 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58bbe4b2-1bd7-3921-846c-479f5076d9d6 | -10.87706 | -50.94965 | 2025-10-09 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4114cc2-731d-375c-8ee0-6e9aa2698355 | -11.77493 | -45.14997 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce6a7fc-8147-3d75-89b0-4b7148856188 | -8.47681 | -47.2043 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e9a9f8f-2fea-39b6-95aa-eb57fe92437b | -8.55172 | -47.72132 | 2025-10-09 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 063a7147-6f0a-38c1-9cd4-abab4f878234 | -8.17059 | -43.32122 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d15b1b11-73b6-34d5-943d-b9b98a4cd087 | -11.8761 | -45.50162 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d792632b-8fd4-3aee-b7c4-bbebae926473 | -11.88934 | -45.547 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 107d01b1-89ee-3623-936d-3aee39051518 | -7.7638 | -44.02642 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 035955a0-19e7-3d9c-9157-434d52e4b6c6 | -15.13111 | -43.66922 | 2025-10-09 04:19:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ac53db3e-bc77-30d9-822c-52e68f7a5240 | -3.25626 | -39.42579 | 2025-10-09 04:19:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7acd457a-aca4-3ed0-b92d-7e70252a8a45 | -11.32087 | -44.88148 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c93972e-0499-3b27-9b81-26d311e03463 | -13.7928 | -45.83681 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e1c6cf1-b2ce-3b1c-9f4b-32b607d3568a | -7.76073 | -46.64693 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e04944c3-0f6f-3614-baf0-76e704148460 | -10.09535 | -40.77238 | 2025-10-09 04:19:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2953f43c-aa10-362e-ae58-94f7f2369f5c | -10.74156 | -50.06262 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 862cd311-36fd-32e9-a4fc-8fac73abc582 | -8.09448 | -44.82061 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1752ed4e-569b-30ce-9d1a-b8b25d9f884a | -7.689 | -42.96675 | 2025-10-09 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9fcee5a8-0416-379e-8743-47090fa3714d | -8.51239 | -44.23347 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34af5cd4-68a8-358d-95de-2b990a889f98 | -8.15827 | -43.32724 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d594df6-3d94-3d3b-868f-78642079dbea | -11.7765 | -45.0525 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aad47ae9-6b63-3bd8-8841-c8ecee2d1298 | -9.76139 | -47.71003 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aff4938-0ee6-3cb6-b055-b12f4fc0fc83 | -8.60823 | -45.09463 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d819dd78-2bf1-3b7d-a9e3-84b8d1ecf967 | -7.82099 | -45.19688 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d967e245-7242-37dc-8533-5c744f9f1158 | -12.06926 | -45.74192 | 2025-10-09 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00a07bc7-ab3c-3d7a-b968-94537363abff | -10.73294 | -50.0662 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 701e3c5a-0c33-310c-af58-5de86bed583c | -10.18801 | -44.54716 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5df915e2-7f94-33c7-9138-8157e2ab558e | -8.83143 | -44.43091 | 2025-10-09 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49dbf6b2-9744-38fe-8e41-ac0f4764826a | -11.83818 | -42.4726 | 2025-10-09 04:19:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b9905fc6-be82-3202-9dcb-8132c16254f4 | -8.20054 | -43.35201 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 826e6d77-a5b8-39ac-9ad5-9894c6cb2160 | -10.73768 | -50.06193 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 662ffb86-c39f-3c39-bfeb-bd1b4e17efb5 | -13.79887 | -45.84144 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 249f2b7c-85b9-3c09-a059-d966f1cd91c6 | -10.09073 | -40.77678 | 2025-10-09 04:19:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0da63cd-bbbb-3f30-b19c-0da5540eec6d | -10.85884 | -49.91862 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d95aaed4-3168-3f5f-8e80-fbeee14828b9 | -9.2221 | -47.8545 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b862adab-83de-3f2b-8c0c-2e297eb6f1b2 | -14.73392 | -46.09248 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 54f8c2fb-f572-3e07-a3f2-bce2c3742d7a | -12.22988 | -43.78254 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e62dee89-2d35-3ce2-912a-f4fcec52ec30 | -11.72519 | -44.30096 | 2025-10-09 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad84612e-d36d-3e67-940f-318f4f9046d9 | -10.87297 | -50.94889 | 2025-10-09 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e6f1449-9afd-3741-83cc-7498cedd0ebe | -12.24355 | -43.78527 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4272dc3-9ba3-3029-8b17-d4cc3fadf6a2 | -11.76221 | -45.14432 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7eba72f5-cf41-35d7-8ce7-339bc1520538 | -11.79923 | -45.03782 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f293b51f-f1ac-3f6b-8b40-f93d2668e5f1 | -13.81102 | -45.82886 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dd85ce2-39dc-392f-b35a-e22eb47613b9 | -7.76936 | -44.03448 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8195d979-0acb-37a3-ba33-399dbc6b0478 | -8.62733 | -48.60804 | 2025-10-09 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9355a71a-7db9-3c51-a361-6b14c5f82115 | -10.86423 | -44.63131 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9746ff3-fa51-3cd4-8c02-e4f32db56c76 | -9.6589 | -43.84258 | 2025-10-09 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84cf6f50-5d9e-319b-8afb-29f16aa92c79 | -10.65582 | -45.09751 | 2025-10-09 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7454b22b-a3de-31c8-9dcf-c3ba812fc496 | -13.47899 | -42.0267 | 2025-10-09 04:19:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README42.md)
