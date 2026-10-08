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

## Dados Diários - Página 258

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6667595e-5917-3741-bc35-48696a49e8f0 | -18.68491 | -46.1576 | 2026-10-08 16:16:00 | NPP-375 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 177e7b3b-436c-3eba-a92d-74fd427144fa | -19.07718 | -48.64501 | 2026-10-08 16:16:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ae39230c-bec5-3ed0-b3fd-6638b6ae1612 | -15.95162 | -41.0902 | 2026-10-08 16:16:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 03145e3b-babb-39e8-8687-b68ae01b039d | -16.94566 | -49.0249 | 2026-10-08 16:16:00 | NPP-375 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acfc41a5-5d05-3fca-abad-6e59d863492f | -15.34217 | -41.04318 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 31ca2c42-73cf-34ac-b75f-1e557e5daf10 | -16.43339 | -40.26915 | 2026-10-08 16:16:00 | NPP-375 | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0fc744c6-40a9-309d-a2d6-848e4c12c016 | -14.41949 | -41.51581 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3dfcc1ca-9943-3e8f-8621-18ac10ae04ca | -20.24217 | -42.07067 | 2026-10-08 16:16:00 | NPP-375 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 2391e435-519a-3381-8e16-c36f6c262d97 | -15.573 | -42.89292 | 2026-10-08 16:16:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8916814b-9602-3a2e-9f83-096be20e2f00 | -14.75849 | -41.32531 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 30.4 |
| a790dd46-7724-3329-b6d7-d9c7717465f5 | -15.40098 | -44.33549 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d9f6be8f-fc93-3152-9454-29f80dca4ca6 | -15.76746 | -40.33876 | 2026-10-08 16:16:00 | NPP-375 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 09e21ce1-55de-39dc-9d9b-64137be5f297 | -15.33843 | -41.04372 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| f1183af3-0413-34f3-91fa-2c6638dd5a13 | -18.05734 | -42.49475 | 2026-10-08 16:16:00 | NPP-375 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1dc69554-4fbf-30ee-83e1-100ea94706e5 | -15.72176 | -38.98651 | 2026-10-08 16:16:00 | NPP-375 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 16dfd7df-7b10-3c9a-b464-d0a959bc3234 | -14.82182 | -39.40487 | 2026-10-08 16:16:00 | NPP-375 | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| b78f321d-597f-3bf3-ae32-1f6314216304 | -14.09912 | -41.20104 | 2026-10-08 16:16:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8aa8f2d0-6cc8-309b-aef3-c3dd1a450d73 | -14.59773 | -41.30285 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4bc5eab5-4553-3640-acba-a1aa7eee27ad | -14.4662 | -40.7254 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| bca1d5f3-8b19-3031-8642-f8325c81eca7 | -15.31644 | -40.64833 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c49743c6-cda6-3b7b-ba31-263ef501b543 | -15.74008 | -47.35818 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99f7d30c-7fb1-3b09-abac-b5886e82418f | -16.97564 | -41.22786 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 52249ecc-7014-38b7-89e2-2fd2521c7edc | -14.78975 | -42.83582 | 2026-10-08 16:16:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| fd152ea4-3e29-3233-8d6e-3f056f50f226 | -16.58915 | -42.43167 | 2026-10-08 16:16:00 | NPP-375 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6806b251-71ca-3290-bf24-89930177d19d | -15.34336 | -41.69632 | 2026-10-08 16:16:00 | NPP-375 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e2c1c652-62ee-37eb-ac1d-bca7c326eba0 | -15.03037 | -42.77917 | 2026-10-08 16:16:00 | NPP-375 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5326d6b5-1857-3308-b95f-84e615617bc4 | -14.46559 | -40.72181 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 31.1 |
| eeb96f38-da04-3bba-ba81-8e989c2fe45a | -17.5813 | -42.27404 | 2026-10-08 16:16:00 | NPP-375 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f63b3cce-b7fe-35a4-8be8-c83b1f1911ae | -16.76031 | -40.99491 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| b3bd3a86-7590-333f-9248-530ef7cc6c32 | -15.83352 | -43.29025 | 2026-10-08 16:16:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9dbe6c66-cc72-370f-a9a3-9c99b93cbcc0 | -18.28051 | -41.23281 | 2026-10-08 16:16:00 | NPP-375 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6d87e1e8-40cf-354e-ada7-5d075de39b99 | -15.00687 | -40.82077 | 2026-10-08 16:16:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9b263497-3f67-3930-84bb-0df2126773bb | -15.04401 | -42.4096 | 2026-10-08 16:16:00 | NPP-375 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64c3d338-d14f-37c9-9284-f0355117e85c | -15.76367 | -41.77297 | 2026-10-08 16:16:00 | NPP-375 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| f479c16f-c8bc-3758-bab2-9d8b5693e4c9 | -16.43771 | -41.27874 | 2026-10-08 16:16:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8ae84ca8-929c-3a17-bc65-3cc38f7f6dd1 | -16.51447 | -43.14816 | 2026-10-08 16:16:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 748634bf-d315-3550-b407-3809efde34c7 | -14.43921 | -43.92818 | 2026-10-08 16:16:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| adb21a06-341c-31f2-a1ce-8f48bd495f23 | -15.34262 | -50.57785 | 2026-10-08 16:16:00 | NPP-375 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92b62308-89a8-30bc-a3e8-b0b47812a1cc | -16.01197 | -40.65912 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 815a6d4f-1cda-3a95-8e8b-39f106e02e01 | -20.64452 | -43.32223 | 2026-10-08 16:16:00 | NPP-375 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| adc60e42-318e-3775-b201-f815939ca46a | -16.11215 | -40.79843 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 52f607ae-34ad-3bff-93fa-e74dad1caf78 | -18.38459 | -40.31753 | 2026-10-08 16:16:00 | NPP-375 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 401d571b-2406-3384-83ba-89ce26b8cfdd | -15.69342 | -40.47187 | 2026-10-08 16:16:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| f0a84a3a-8d00-3348-864b-6be731abc266 | -14.85276 | -42.06698 | 2026-10-08 16:16:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f3cb2db-48f3-3074-b5b8-a2490e5bb286 | -17.47298 | -44.36345 | 2026-10-08 16:16:00 | NPP-375 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b7e4a3c-b7e9-350d-9ada-f9c7f415d880 | -14.55393 | -41.34723 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 889e496d-5c00-334b-932d-230900bab4d9 | -17.69722 | -39.17049 | 2026-10-08 16:16:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c262431e-39bc-3ad1-8398-93e787b896d8 | -15.7717 | -40.34268 | 2026-10-08 16:16:00 | NPP-375 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 62c14f97-8a6f-3638-bc11-19ad82ee57e5 | -15.39579 | -44.33126 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cce0b0a2-2610-3b39-88ff-f616934f8eae | -18.04778 | -44.60471 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| edc136e8-8ad8-37e5-8785-4c411279126c | -17.11753 | -41.33649 | 2026-10-08 16:16:00 | NPP-375 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 1d35e46e-1592-3fa1-b287-881e0b14dff0 | -17.78242 | -43.99976 | 2026-10-08 16:16:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e04cdd76-2e9f-3e14-a9e7-b6503affbf1e | -14.67356 | -42.48116 | 2026-10-08 16:16:00 | NPP-375 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 74c2a607-4ffe-3a4f-a6f0-d4bd582ee5aa | -18.38831 | -40.31699 | 2026-10-08 16:16:00 | NPP-375 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f1d0a075-e678-3f6b-95ef-c7a1c7a4d970 | -17.64786 | -44.28411 | 2026-10-08 16:16:00 | NPP-375 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 19e373d4-6431-3adc-9650-fd0832f99dd0 | -15.73026 | -39.66323 | 2026-10-08 16:16:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| b429cbd4-6021-31f4-982c-fc1be0c34039 | -15.47168 | -47.64527 | 2026-10-08 16:16:00 | NPP-375 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b3e732b-d8ac-3514-bb10-0497c972db75 | -16.97949 | -41.22733 | 2026-10-08 16:16:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 5e10dd55-3b97-3e89-9bdf-1c4701adfd3c | -16.58869 | -46.75906 | 2026-10-08 16:16:00 | NPP-375 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac2df046-5715-3c82-8165-54369c1fd1b7 | -15.83086 | -45.39984 | 2026-10-08 16:16:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17d57432-8f23-393e-bb23-0c872a9ae434 | -15.10954 | -43.63134 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 277ed2c8-bfee-3bac-9b7a-41b687ec5d21 | -14.53352 | -41.67643 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 33a06889-0a8b-3d34-850f-489e001b3afa | -14.09958 | -42.47848 | 2026-10-08 16:16:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 0d22f0c9-710a-3354-b7dd-02bca72d782c | -15.50631 | -40.70108 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5a677adf-0c43-398c-8634-ca5c00f29f75 | -18.05348 | -44.56902 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b89abc0-35b8-3eb7-b892-65945d1f0879 | -15.79162 | -44.6818 | 2026-10-08 16:16:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 261.4 |
| 88268530-a5af-3989-b285-6298c98a5f87 | -14.44145 | -40.78678 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a6fea01e-048d-3a96-a03d-d28b2d16d272 | -15.82907 | -40.48772 | 2026-10-08 16:16:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8fdc3dd1-b34e-3855-9f4d-82f4fc3dcb90 | -14.44363 | -43.92762 | 2026-10-08 16:16:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 94b32c89-841b-360d-a144-05d42c132e83 | -18.2962 | -42.88675 | 2026-10-08 16:16:00 | NPP-375 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 396a3de1-edb7-3c80-b52d-117f03797c82 | -16.65068 | -46.26656 | 2026-10-08 16:16:00 | NPP-375 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffa7502a-a9ce-3724-abdf-d5abc7d6efa2 | -15.82778 | -45.41167 | 2026-10-08 16:16:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b9bacc83-f687-3b07-93a6-d9d39f798aa2 | -15.96813 | -40.69682 | 2026-10-08 16:16:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5f229630-da13-361e-974c-781fd93642ae | -16.18973 | -44.56676 | 2026-10-08 16:16:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8080d07c-66fd-33ed-888b-5b871055e601 | -18.05783 | -42.49882 | 2026-10-08 16:16:00 | NPP-375 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fcdd93fa-2f2f-30f5-82c3-a712894a6e54 | -14.59671 | -41.02109 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 075797b8-ebc1-39aa-9673-e90fff2ecbae | -14.6988 | -41.00671 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fedfff07-0a64-37a9-af0c-4b3838580a25 | -19.25765 | -40.73954 | 2026-10-08 16:16:00 | NPP-375 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 69b9a539-c53d-32df-ab90-4b74d1162986 | -14.44749 | -43.92271 | 2026-10-08 16:16:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 21d86db5-5de8-377a-b634-8c4c09111d85 | -18.26257 | -42.18258 | 2026-10-08 16:16:00 | NPP-375 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 3a189ebe-a12f-3462-ae82-0bfa9eacd43d | -15.54354 | -43.1712 | 2026-10-08 16:16:00 | NPP-375 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 9cefec5e-ce4c-33cf-918c-66f3e8bd3233 | -15.5379 | -41.72087 | 2026-10-08 16:16:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| a15f0198-1d99-3a61-8ff2-b56089437f3e | -16.35238 | -44.71538 | 2026-10-08 16:16:00 | NPP-375 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 54a57535-1862-3cd7-a5b4-9174975d2778 | -14.4182 | -41.50643 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 346fe543-c08e-3a69-aedd-ce4f3c6ad114 | -15.5735 | -42.89682 | 2026-10-08 16:16:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57e25326-b6a6-3cd0-a26e-c1f11f2bbe0a | -17.00678 | -42.37915 | 2026-10-08 16:16:00 | NPP-375 | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ce6e5ea-bd1b-35ad-8cd7-96a9e2421fe5 | -14.98947 | -40.48064 | 2026-10-08 16:16:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| dd86a0da-4244-3cc2-a0af-f1fdbf7bd939 | -20.47653 | -44.2212 | 2026-10-08 16:16:00 | NPP-375 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6c2de18d-526c-30db-8df2-40af7e2d5535 | -16.48794 | -39.11102 | 2026-10-08 16:16:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 253bc325-6a7c-39f4-a01c-ace1d91310f9 | -15.39637 | -44.33608 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 110a2d1b-cc95-3f64-b9a9-846c2ef32348 | -14.46798 | -41.2503 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| b0a1df29-5e28-3ac2-89bd-a077fc6a72ab | -17.9814 | -42.86164 | 2026-10-08 16:16:00 | NPP-375 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06dcc91e-716f-3fc6-bbb5-f0276397b9f7 | -14.89519 | -39.72892 | 2026-10-08 16:16:00 | NPP-375 | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bdd3d373-ab05-3cbe-b71b-b07e082008af | -14.64141 | -41.23191 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a0220e2e-1d93-30cd-998d-9e989c742348 | -15.08892 | -41.35388 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| f33c5d39-6353-350b-b8e9-2025a82cfac7 | -14.49806 | -40.82328 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 91c92549-415c-3455-9ee1-dba9957d7d7b | -15.65578 | -43.26588 | 2026-10-08 16:16:00 | NPP-375 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ae34f8d7-a3bb-395b-bfb0-95019b28be1b | -15.70825 | -41.02075 | 2026-10-08 16:16:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 36c673ac-63b3-3dbc-9167-c69695f36ae1 | -15.11446 | -43.63508 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 55.0 |
| c05cdfef-d7d9-328a-b8bd-7be3d4b17f0e | -16.93452 | -42.10585 | 2026-10-08 16:16:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |


[Clique aqui para ver as próximas entradas](README259.md)
