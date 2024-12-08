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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df586168-df80-3ff5-b410-25c39d978f6b | -7.80727 | -46.22875 | 2024-12-08 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 652b18f1-ed83-339a-bfc6-c32ee103768f | -5.90709 | -48.03119 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85014a85-ffc7-315b-87cb-17f5d7dd7628 | -9.99839 | -42.17456 | 2024-12-08 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4dd996d-3e79-3fb3-aa6e-22c3e7d7a2bc | -6.36108 | -44.00652 | 2024-12-08 04:14:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65cdbeab-1972-3a0f-b6f7-b2f951d94583 | -10.00124 | -42.17881 | 2024-12-08 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 578beae2-5902-34b1-a7c4-4ed342391d2b | -12.39907 | -46.59336 | 2024-12-08 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cf49272-8144-342e-8b24-82e0fb541c65 | -10.43994 | -44.88955 | 2024-12-08 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c39d698d-5e5a-3f86-910b-21d12c44d909 | -8.05123 | -47.9084 | 2024-12-08 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 326ad10e-4b0d-3b7a-9a88-3b8ae9c0d798 | -5.77806 | -42.59912 | 2024-12-08 04:14:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c1fd3f8-7242-3f43-a161-d3a03183d122 | -7.80304 | -46.23222 | 2024-12-08 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1fd2f2a-ef51-321e-925d-a155fb8fb260 | -6.87299 | -47.24109 | 2024-12-08 04:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e71be845-3699-34c7-9151-891fa0f64d07 | -9.25927 | -48.67612 | 2024-12-08 04:14:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d82f189c-6c24-308c-8061-017f28f655d1 | -6.65643 | -47.52635 | 2024-12-08 04:14:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 599f93c2-c9d4-3c2b-b582-8e29b4f4751b | -10.4472 | -44.88707 | 2024-12-08 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccaace40-e916-3e03-8e51-ddbe2eab5847 | -6.93919 | -43.53889 | 2024-12-08 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5ec214d-bac2-3b41-8aec-849695694aae | -10.44051 | -44.88599 | 2024-12-08 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 719ba75b-26d6-33be-b5ca-7253887cca37 | -5.49446 | -46.76999 | 2024-12-08 04:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3425b519-1808-3394-b6b8-f90eda011095 | -7.80794 | -46.2247 | 2024-12-08 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae54c4e1-ff3d-351f-9394-e4f770c7bb06 | -10.44386 | -44.88653 | 2024-12-08 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7335035-a27f-3b3e-92cc-289c9f4010ec | -5.91173 | -48.02828 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bf6e462-0a28-325d-a24e-2230801b1aef | -10.00613 | -36.3339 | 2024-12-08 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb1e0921-e412-3568-ab13-0b0ce5e59a6a | -5.50039 | -46.24731 | 2024-12-08 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afa324a2-24d8-36c3-8e19-50169377b59e | -9.37294 | -46.3029 | 2024-12-08 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ad840970-e180-3603-989b-edc60897aa6f | -10.00058 | -36.33864 | 2024-12-08 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20835948-fc70-393a-8fc9-e20717adbb50 | -5.50404 | -46.24794 | 2024-12-08 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a56e7b1-02fc-3188-9ccb-e45f57933550 | -6.20634 | -46.06253 | 2024-12-08 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eae3e21-261e-3f96-8d1c-633bf244db1d | -5.42845 | -44.70905 | 2024-12-08 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f214a166-6f8f-3a19-a910-18c11bec7782 | -6.98747 | -47.08815 | 2024-12-08 04:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14191154-2518-3eb5-98e6-bd9de8ff3ded | -8.05192 | -47.90141 | 2024-12-08 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a3ca4d4-3631-3310-8927-e08c645b829f | -5.5279 | -46.96244 | 2024-12-08 04:14:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a0c33da-7ae9-39c2-b842-e818d8147635 | -7.99477 | -35.31344 | 2024-12-08 04:14:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 03369280-7fbd-367b-87aa-013bf1d595e4 | -9.22166 | -50.69359 | 2024-12-08 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c2cd575-8aee-32dd-b1b8-fad7cd48dce0 | -4.56628 | -48.02927 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 155e5464-4334-395f-92aa-fdb27f68f943 | -11.15847 | -49.70124 | 2024-12-08 04:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3458ad2-9c76-32a8-9da2-767659678863 | -9.21896 | -49.48386 | 2024-12-08 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e152f851-0d5e-3b86-8b2c-238cc84959b8 | -9.99782 | -42.17827 | 2024-12-08 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ac1dd8b3-2b54-325c-8223-a08adfdaf145 | -4.58264 | -48.01996 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a11a50f2-795e-3d01-8dd5-4268398f0579 | -5.42561 | -44.70478 | 2024-12-08 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f95ef2c3-2a64-3222-a92a-be45a7d37a7a | -4.58139 | -48.02745 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 717e1373-b67b-3f79-a2b5-c35e05d0a1fc | -5.42796 | -44.70906 | 2024-12-08 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f31229c4-2c19-385a-9993-4fce4d9bda58 | -9.11339 | -49.47053 | 2024-12-08 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfd21414-214b-3afa-8286-24aff06723e0 | -7.88008 | -44.20499 | 2024-12-08 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ebdb636-f9d9-3fe0-95a1-791fdc114e97 | -8.05112 | -47.90627 | 2024-12-08 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee739bc8-2d12-3c70-aba5-b9497fbb453f | -5.58014 | -45.21474 | 2024-12-08 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b209ce1-0e4d-3365-ad7d-61c321b26cbd | -8.15633 | -42.94313 | 2024-12-08 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 25a28d27-fa02-3993-91cd-81da7f12a3d2 | -5.92447 | -48.02661 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b71d314-a475-300c-bf06-13d86da65110 | -9.954 | -41.37212 | 2024-12-08 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9bf5f92a-8c38-3b3e-8c2e-ddbd7243834f | -5.19878 | -47.74314 | 2024-12-08 04:14:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe67e9c-c767-31aa-bbe6-76c8bfb6a83f | -10.0018 | -42.1751 | 2024-12-08 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 397ccc02-540d-3e77-b025-679f9c263b6f | -5.50437 | -46.24961 | 2024-12-08 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 121c9f19-25df-3820-ab1a-6732b951c6a6 | -10.00538 | -36.3394 | 2024-12-08 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ba8bd40-33cd-3858-9b87-f885e3dae397 | -5.55182 | -42.8756 | 2024-12-08 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 374ee774-f397-30ce-a403-0c826ead8efb | -5.50071 | -46.24899 | 2024-12-08 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62571ce5-516b-3510-bd86-fcd5c4f8bb36 | -5.53466 | -46.45213 | 2024-12-08 04:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e0779f4-1849-3f29-8a56-8fecb760dcd8 | -4.56901 | -48.0254 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc40a842-21a6-3c7c-bbaa-20c9809e4c0d | -5.53799 | -42.87698 | 2024-12-08 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 464babdd-1eef-3072-9b38-3a015cb0af39 | -6.31046 | -47.34281 | 2024-12-08 04:14:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38fb1884-f3e0-39a7-9280-4727720b5f6b | -6.9879 | -47.08596 | 2024-12-08 04:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db973f7b-0220-3370-a8ac-a275f3894484 | -5.62775 | -46.89586 | 2024-12-08 04:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 970bccc8-eea2-3534-ac30-14331000ec04 | -6.68619 | -47.66168 | 2024-12-08 04:14:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 22188774-9b98-3ea1-918c-64761b7540f7 | -6.0536 | -44.04861 | 2024-12-08 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 662a3dfd-9c21-37b3-8626-541a04526319 | -6.28769 | -43.85069 | 2024-12-08 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a45d880d-e646-3129-86bd-b5b97a5a41a5 | -5.91114 | -48.0318 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17ce02ca-2cd8-3be6-a138-fdfa67001a18 | -7.80371 | -46.22816 | 2024-12-08 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8605ae00-0fef-317e-be34-ab4d01ead8c6 | -5.19477 | -47.74246 | 2024-12-08 04:14:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0efaa689-ec82-3881-8d52-db001ea92a16 | -7.79707 | -46.20212 | 2024-12-08 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a66cc393-5ec4-3bf9-8959-a01a819dfe3f | -7.99078 | -45.79569 | 2024-12-08 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1f99d2ec-97e5-3ede-9791-b2e0c5092ed1 | -4.56689 | -48.02546 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f061b547-2b4b-33ed-a3b6-0a55993aff70 | -5.58076 | -45.2109 | 2024-12-08 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63b8bbe4-87a2-3752-acfc-d77309a28f04 | -5.92389 | -48.03013 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9832e8c4-e5a8-3b5d-89c9-da5f568ba0e2 | -9.9544 | -41.3711 | 2024-12-08 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 429b876f-238c-3e82-ae92-44649747728c | -7.52831 | -47.29969 | 2024-12-08 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaf03952-39f4-31c5-9e5c-b4ed417ebcec | -7.88342 | -44.20553 | 2024-12-08 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fed8284-2f78-3716-82da-99cc5b3654ed | -5.63922 | -46.73175 | 2024-12-08 04:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5278010d-063d-3067-8484-808732e5bbd4 | -12.40252 | -46.59396 | 2024-12-08 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faeb9360-03a9-3c67-9968-36375bdd61a9 | -9.37963 | -57.55315 | 2024-12-08 04:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 038370b1-007d-32a6-b3b9-c886ae0f06ef | -5.81488 | -42.49445 | 2024-12-08 04:14:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bce3373-7f3b-339e-8431-b61d5ed2732e | -11.34091 | -38.14297 | 2024-12-08 04:14:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef52095e-4866-3ddd-b325-75ce78bfd721 | -6.05081 | -44.04455 | 2024-12-08 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4192e636-10da-3647-9a32-a14aee4bb28b | -6.29102 | -43.85123 | 2024-12-08 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86659463-77a2-3604-a966-7a257483cceb | -5.76654 | -46.85013 | 2024-12-08 04:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 446d35b9-d1d9-3e18-9587-3b5a09174864 | -5.77473 | -42.59861 | 2024-12-08 04:14:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 089b7b20-5831-328a-bfea-dc804a19b9fd | -9.21474 | -49.4831 | 2024-12-08 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 814d248f-2d30-3234-9c69-6b3b9d81a568 | -5.64296 | -46.73239 | 2024-12-08 04:14:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69b49618-2df7-3657-9393-64d32234fcd7 | -9.21249 | -43.0654 | 2024-12-08 04:14:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86d95ad5-5b96-3713-834e-a78610b42b11 | -6.68554 | -47.39812 | 2024-12-08 04:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fe4b3f0-45f5-38c5-aa23-39fa638d036f | -6.55313 | -44.20387 | 2024-12-08 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be9d8f16-8591-3007-98c5-7095f390290b | -6.98372 | -47.08752 | 2024-12-08 04:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 678e1e2b-5c9f-3935-94f6-10e1e2322c68 | -9.10985 | -49.46586 | 2024-12-08 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0535d6eb-e7b3-340f-b8c5-67707a8ab381 | -4.58202 | -48.0237 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 08e5353e-c11e-36ad-be31-5185c496be83 | -19.43943 | -44.3412 | 2024-12-08 04:16:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12a0bae2-b464-3824-92a5-18cac198ab7c | -12.69541 | -46.76516 | 2024-12-08 04:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53583d9c-2652-3a89-8dca-699e9d42ea2a | -17.09466 | -43.80476 | 2024-12-08 04:16:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 999193a9-112b-3bff-8dc3-dda442667095 | -12.69194 | -46.76456 | 2024-12-08 04:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfba1374-d8c7-30a2-84c0-9969ea838473 | -15.37006 | -53.12897 | 2024-12-08 04:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61300061-411c-327c-b3a2-aff53347f65e | -17.81052 | -42.94338 | 2024-12-08 04:16:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3f2eb43-4117-3629-95e2-33b42936a93f | -12.8593 | -51.94441 | 2024-12-08 04:16:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 574a172b-a070-3d88-9274-984b5ad19df6 | -15.57863 | -46.56124 | 2024-12-08 04:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a49c955-71b8-3855-ba62-52250f254109 | -12.41313 | -49.69233 | 2024-12-08 04:16:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac48538f-f719-3c26-845a-387fa9f2fa12 | -12.40357 | -49.67555 | 2024-12-08 04:16:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
