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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c2828a7-70d1-37c7-88a8-0a3cb41b535b | -20.11162 | -43.51788 | 2024-10-04 04:36:00 | NPP-375D | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 8cccd1aa-3cea-388d-97c8-4f56b1a592e7 | -20.111 | -43.52332 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7ddedc09-2116-3949-8388-001bf4c84794 | -20.11036 | -43.52901 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e0ab0216-8ba2-336f-a7c5-823b51877ff9 | -20.10631 | -43.52294 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 54fb12b5-148a-3f12-84fe-e3e020710d1f | -20.06499 | -43.6088 | 2024-10-04 04:36:00 | NPP-375D | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3b69fc95-fad5-3791-abed-27cc91647f91 | -20.03416 | -44.14838 | 2024-10-04 04:36:00 | NPP-375D | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 4a3eb41f-b0c6-3d99-af72-93e1fa76466e | -20.01136 | -44.49132 | 2024-10-04 04:36:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3ba2991a-b10f-35ac-b1ac-43ddf813cfcb | -20.01081 | -44.49593 | 2024-10-04 04:36:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 40ffb9a1-0ce2-3ce3-bbb5-9b7254c13302 | -20.00698 | -44.49084 | 2024-10-04 04:36:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 48231081-c596-3bfa-82c5-2564d1bb4c37 | -20.00644 | -44.49536 | 2024-10-04 04:36:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a3467a3f-bd29-343d-8ba5-3579cd8116a7 | -19.98328 | -43.54139 | 2024-10-04 04:36:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f35e04ed-6f5a-380c-ad4a-05b79895e3c7 | -19.97863 | -43.54075 | 2024-10-04 04:36:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 06f229a4-128d-3c1e-920a-a88c39b43dff | -19.89166 | -44.52246 | 2024-10-04 04:36:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d727e58b-780f-35bb-909a-52201acd63d7 | -19.89115 | -44.52676 | 2024-10-04 04:36:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 34ae9436-7392-3d14-8e6f-280f1d4f7c65 | -19.88676 | -44.5264 | 2024-10-04 04:36:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f59b464-d4af-3cb9-b42a-4266561d5a82 | -19.65318 | -44.90203 | 2024-10-04 04:36:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4d9c0915-3b56-3ab8-b069-6709c99c09b6 | -21.63134 | -44.47498 | 2024-10-04 04:36:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcf839ec-2714-3b35-8643-94b2891af8a1 | -21.31798 | -44.8347 | 2024-10-04 04:36:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dbd67e4a-1ac1-399d-9ede-4059a3a65596 | -21.31413 | -44.82976 | 2024-10-04 04:36:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d317e049-b288-3b99-bf3b-88b7eaf3d679 | -21.31362 | -44.83415 | 2024-10-04 04:36:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9aa719b9-e1d5-3d4d-b332-da871f37bd88 | -21.19546 | -44.93567 | 2024-10-04 04:36:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a60ac5f6-5a7c-35e7-a262-324cb2338752 | -20.76534 | -46.29516 | 2024-10-04 04:36:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e915017e-9759-36c7-b7e7-ec81957f20a7 | -20.76464 | -46.30052 | 2024-10-04 04:36:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b43b04b-4fad-316f-b354-b294feda56bf | -20.72711 | -46.61764 | 2024-10-04 04:36:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3de9e8e-61aa-32bc-99f6-e6df15fa48cf | -20.51101 | -46.38646 | 2024-10-04 04:36:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6925642-44be-3c34-8ba9-0ed9ac577b86 | -20.51023 | -46.29938 | 2024-10-04 04:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 608b4866-1856-3889-baa8-fcadbc827c9d | -20.50773 | -46.38099 | 2024-10-04 04:36:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8d80250-4e54-3d62-87b9-aa42a1f8e1e0 | -20.50709 | -46.38603 | 2024-10-04 04:36:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a6da12f-1e77-3c92-bf76-3caf5fab0781 | -20.36234 | -46.33857 | 2024-10-04 04:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 434103fd-ac67-39de-862d-cccbaf4fd44b | -20.36196 | -46.34222 | 2024-10-04 04:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f42c3fca-a768-3091-acf3-0fce20e62550 | -19.66504 | -46.23281 | 2024-10-04 04:36:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a631691-44d8-31cb-b26c-55cdcc5df48c | -19.66113 | -46.23231 | 2024-10-04 04:36:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 689ea8e5-1250-3424-a131-962e558ee7eb | -20.24113 | -45.49944 | 2024-10-04 04:36:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 689995e9-682e-3172-b373-3d1ffbebba4d | -21.44536 | -46.56407 | 2024-10-04 04:36:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1739f3ba-07dc-3c85-8291-032b7f6a2118 | -21.44472 | -46.56908 | 2024-10-04 04:36:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2df2bf10-6f0a-3ad0-b848-17f855598983 | -22.73498 | -47.03813 | 2024-10-04 04:36:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1e619164-e133-3527-835a-3f07f6b6272d | -22.73469 | -47.03624 | 2024-10-04 04:36:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3b09c48e-25bc-3e15-8eac-4a9d51f2a0cb | -20.27081 | -46.87613 | 2024-10-04 04:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce48a6d5-334c-3cb0-9c6e-0bcb9e9cb334 | -20.26704 | -46.87546 | 2024-10-04 04:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a957c32-771f-3a03-824b-571a47adeb19 | -20.19388 | -47.46649 | 2024-10-04 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a25dad65-4612-3c7c-b755-780b65533cff | -20.1908 | -47.46169 | 2024-10-04 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67573f69-3839-3fd0-82ad-e5c291a34877 | -20.19021 | -47.46594 | 2024-10-04 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97ad3aeb-74bc-3654-8159-c5f6e5c67385 | -20.18963 | -47.47015 | 2024-10-04 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 51f3d1f6-7a07-3d6a-bf56-9c0907d75c3f | -20.18653 | -47.46545 | 2024-10-04 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7b32aa2-3fb1-389d-89e4-4a2d2f451d52 | -19.75767 | -46.67217 | 2024-10-04 04:36:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ff61e0a-7584-386e-a09b-e0b0ecd8fe1b | -19.75388 | -46.67149 | 2024-10-04 04:36:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84e6b23a-6ba2-3ffc-9b93-f780071a5d12 | -19.75193 | -46.68597 | 2024-10-04 04:36:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0cc9ecc-f7db-3f8f-ab13-b615466558ab | -19.75129 | -46.69077 | 2024-10-04 04:36:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60ae81db-9edc-3557-adc9-a32c75a0eed3 | -20.72038 | -46.90207 | 2024-10-04 04:36:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f5aed95b-49dd-3119-ad1a-f9e0b1b8d671 | -21.92311 | -48.40886 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe30b66b-bcdc-3b23-a758-25df71184cef | -21.92253 | -48.41309 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2862837-a7e5-3a59-b82d-ebfd96edb872 | -21.9196 | -48.43453 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e29715-3d7c-3a32-8720-22f3f5abae07 | -21.91895 | -48.41254 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53bf69b1-4e0d-38eb-a623-906546dd3dbf | -21.91788 | -48.41023 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf32ada1-68d1-3c82-98e5-b480141c208f | -21.91728 | -48.41447 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5648a66b-6ccb-3b5c-a7b8-26517e26c32d | -21.91603 | -48.43399 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41f4899b-22c8-36bb-958e-6e1edb26175c | -21.91537 | -48.41201 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1595d6ea-4baa-3cc3-861a-f6699aab8428 | -21.9137 | -48.41394 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84b19588-fe86-33b0-ac5d-78195f2d0357 | -21.91121 | -48.41576 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20ee2594-1c73-32b9-a411-8ccf19acebc1 | -21.91011 | -48.41343 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81faebda-acd2-3853-9f93-8121a57dc47e | -21.89993 | -48.43384 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7fc2613-ed84-3767-b370-a1c63870880d | -21.89806 | -48.47301 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32b21f6d-fee8-34ec-a736-5ce54e96208e | -21.89746 | -48.47725 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed6f944-62f5-35d0-9f18-7e063134de42 | -21.89635 | -48.43333 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab832cd5-993c-3c4f-85d5-dbe6259067c7 | -21.89388 | -48.47676 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74e39cfb-5120-37e3-8f58-aa61ee9993ac | -21.88971 | -48.48051 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5f50073-1648-322f-b5ca-72e2786a9c86 | -21.88745 | -48.41866 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5448f325-8180-33d4-9899-2f24f5fa1002 | -21.88685 | -48.42296 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 21116019-24cb-363f-914f-f693e6490353 | -21.88388 | -48.41809 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cfcabb24-0ae4-35a5-892b-0cfc0735acbb | -21.88328 | -48.42237 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f5317f2-c1de-3825-8db2-34df5ba39f6f | -21.87971 | -48.42179 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ace556b0-a4b2-35dd-b580-c50a9583a571 | -21.87614 | -48.42119 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e92079f-3b00-33be-9aa2-ba4bc5edcdab | -22.22512 | -48.61505 | 2024-10-04 04:36:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4f0b99ec-3817-3e6e-bcd5-3439877e53ce | -21.50902 | -48.07112 | 2024-10-04 04:36:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a46cb09b-1419-37e7-ac8e-ff92bfc35269 | -21.38288 | -47.62985 | 2024-10-04 04:36:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdd7bcae-1a68-37e1-945f-76c46537d44d | -21.38143 | -47.62764 | 2024-10-04 04:36:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd8ced63-da44-3bf4-8d35-c72c707d51c2 | -21.31309 | -47.60382 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ae89bde-8800-39b8-bfaf-07463829b94f | -21.30939 | -47.6033 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 614b62e6-2fad-3667-b333-8c35e0a8a38c | -21.3088 | -47.60771 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1862d758-591a-38d0-b62b-6fc2171f7e0d | -21.3051 | -47.60722 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43e73847-a9d6-36c5-ae2e-69bd4c088f81 | -21.3045 | -47.61164 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5671114-b304-3eec-a062-4620c017b752 | -21.30328 | -47.62072 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b069f4e8-7b5b-3b65-b804-060c081bd8de | -21.30269 | -47.62512 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8194d5fe-ba65-38d1-b25a-0d33771c622d | -21.30139 | -47.60676 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e40b557-34e1-3dee-9064-725519b59ab3 | -21.3008 | -47.61119 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e214e957-b982-3cb9-9529-48311255b66e | -21.3002 | -47.61566 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26b5c29e-504f-3132-b367-388856734611 | -21.2996 | -47.62009 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f8a6b2c-2fc7-3e6e-b57a-bbbc6423e135 | -21.29901 | -47.6245 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c15a0e1-c236-3b04-a8b4-19ce00a83bc2 | -21.29221 | -47.61908 | 2024-10-04 04:36:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 645046a5-c5cf-3f43-b9e6-b457944e6468 | -21.85116 | -48.36402 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bba7aa1b-1c21-3f0c-af0d-3677b899bc2a | -21.85056 | -48.36836 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89de5526-cd56-33b7-a9c9-100f3f449a11 | -21.84818 | -48.38565 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1021e7bf-9236-379a-8ae2-82871d5091aa | -21.84756 | -48.36357 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c49977e2-f101-3db9-9acc-df879d6fc7e1 | -21.84697 | -48.36791 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f96b93-7517-3d1c-a996-3eb3bb564bc6 | -21.84637 | -48.37222 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0006b5fb-1299-333c-a1bf-a61ae1ab254e | -21.844 | -48.38945 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9259e0cc-8d25-33c1-a034-554516123acf | -21.84279 | -48.37171 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1c75bdd-68cc-3b16-aa8e-38d4ebb74bae | -21.84042 | -48.3889 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e5c6c551-dfe0-3d56-b25d-7e4592342d15 | -21.83981 | -48.3933 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 89912b70-48d3-3f33-96df-67118bb111b5 | -21.83921 | -48.39767 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |


[Clique aqui para ver as próximas entradas](README134.md)
