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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70ed65ce-6085-3ed0-997b-f2c64cf9ddd5 | -22.98319 | -45.52021 | 2026-08-29 04:36:00 | NPP-375D | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 99856bc9-17e4-3d6b-ac6d-43059eb6d65e | -23.23183 | -49.3506 | 2026-08-29 04:36:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 47687fac-6a19-3cac-a4d0-e6ac37f4c1a5 | -24.05205 | -48.64493 | 2026-08-29 04:36:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e1d09b3-96b8-3090-8048-bc713ed40246 | -23.11599 | -46.90894 | 2026-08-29 04:36:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbec7d50-0155-38b6-8a73-a243daa430ca | -19.22422 | -57.66052 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 884e7ef8-4ab1-3b3e-b598-ca3676bcaaf3 | -21.53153 | -48.62277 | 2026-08-29 04:36:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2679fb81-02cc-3d66-8165-cb578494fdf5 | -21.38447 | -45.68508 | 2026-08-29 04:36:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c4ea686-b196-3ba8-8cea-718771ffa879 | -26.68643 | -51.45479 | 2026-08-29 04:38:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2b7e819-792f-3c98-a541-e694ed5d3c11 | -27.56446 | -48.66192 | 2026-08-29 04:38:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dd6167a6-f20b-3dc8-8866-6be0fcd530b4 | -26.57189 | -51.51103 | 2026-08-29 04:38:00 | NPP-375D | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7573891-dd08-3b47-9ed1-cd982abb5ccb | -25.35101 | -49.35069 | 2026-08-29 04:38:00 | NPP-375D | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54b9eddf-75c3-346c-828d-a092e7c98d12 | -25.49209 | -50.48514 | 2026-08-29 04:38:00 | NPP-375D | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 017c102a-bc81-398a-a95f-77602fd4cc9e | -25.05557 | -50.10462 | 2026-08-29 04:38:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8d28c644-e1f3-3eae-b683-1fdccc0c057e | -6.6317 | -43.73 | 2026-08-29 04:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 89d6baa2-1eda-3098-b1ff-69404670376a | -7.5136 | -55.3251 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 026c13f7-fd3d-38de-9bb5-3421b8d11bcc | -7.5137 | -55.3051 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 216.6 |
| 1d6329f3-0aa3-3350-8884-8e5be9a5f272 | -6.77 | -55.6445 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 4abc085e-24d9-3ca3-a1b9-397d23adc3e9 | -7.4952 | -55.3062 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 29972657-b75b-3e0c-aca3-d2572a092725 | -10.4794 | -64.5012 | 2026-08-29 04:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d37d655f-a0cc-3097-8c07-5ea4c4b7d777 | -7.5139 | -55.2851 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| be42e8c0-34df-33f9-b26d-64da73956db6 | -7.4953 | -55.2862 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 52df1bd9-fc65-31bf-b900-d49d0ef7594a | -6.7884 | -55.6635 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f2d626f9-7ae8-377f-a958-238a4b2b6671 | -6.6315 | -43.7533 | 2026-08-29 04:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 57be5f3c-0e7e-302f-b301-a12d92ad03f0 | -6.7699 | -55.6644 | 2026-08-29 04:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 0693968f-63f6-3b50-9d7b-3d7e1cffe7ec | -5.8894 | -57.7708 | 2026-08-29 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f2f25a71-9412-3827-a82d-b46c43c05bce | -5.8895 | -57.7513 | 2026-08-29 04:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| e73a2590-5966-3721-b9aa-47c52cb093dc | 4.11006 | -61.29943 | 2026-08-29 04:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f4900a-4000-3f82-a671-86e9cff0b8b5 | 4.11749 | -61.30418 | 2026-08-29 04:49:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 625b0318-0b87-35fa-a73a-036236da7afb | 2.51791 | -50.85371 | 2026-08-29 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fd71c1a5-89bb-3413-8c41-6dbf314d6940 | 2.52073 | -50.84957 | 2026-08-29 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1124318e-fc18-3072-9391-6763ef342518 | 2.5213 | -50.85319 | 2026-08-29 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd7535ee-36e5-3202-a463-a71d931fc65f | 2.16173 | -50.91177 | 2026-08-29 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f79a7fc0-870c-30b7-be1f-d34c2416ff04 | 2.52187 | -50.85681 | 2026-08-29 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2972117b-77a6-3d31-9388-d42f1f338b66 | 2.51735 | -50.85009 | 2026-08-29 04:49:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f40d9303-3b1d-3235-ba29-5b1cefe645ae | -6.6129 | -43.7317 | 2026-08-29 04:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 9d9af2ad-9002-3ad0-8c8c-dfad1913ea81 | -7.5139 | -55.2851 | 2026-08-29 04:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2c673d2e-4ea3-3bae-aecc-65073c51fe45 | -6.77 | -55.6445 | 2026-08-29 04:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0c427527-ee76-30f0-8971-b707c89d40de | -6.6315 | -43.7533 | 2026-08-29 04:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b94d6829-74f0-3c30-af35-6d40cf8d8404 | -6.7884 | -55.6635 | 2026-08-29 04:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 835c36bc-7af6-33b7-90dc-a51932cf9b58 | -5.8895 | -57.7513 | 2026-08-29 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 1ffaa0df-70c3-3d47-96cc-a7adbf408e4f | -7.4952 | -55.3062 | 2026-08-29 04:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3f124ec6-dfd8-3013-bc2b-bccfb976308c | -5.9079 | -57.7506 | 2026-08-29 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 038c071c-6bd6-3a4e-9424-40a0ab5cb224 | -5.8894 | -57.7708 | 2026-08-29 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e282baa3-c075-3031-aeea-d13d1b562c3e | -10.4795 | -64.4824 | 2026-08-29 04:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 11f828fb-0331-30d8-9634-f2deade5ed30 | -6.6317 | -43.73 | 2026-08-29 04:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c7953897-1e5d-3d45-80ba-e4997e422db7 | -10.4794 | -64.5012 | 2026-08-29 04:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a36494e9-25c5-33cd-8823-8e934c69df7e | -7.5137 | -55.3051 | 2026-08-29 04:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| dfa4372e-86d2-3bf3-bb49-00a919f97083 | -6.7699 | -55.6644 | 2026-08-29 04:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d89a6a33-8c7d-3bf7-9c93-150e497c1278 | -3.60906 | -60.54479 | 2026-08-29 04:51:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8323f48-5c86-384b-8cba-b58acd9e0515 | -2.71912 | -47.05009 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd3c42f6-9cdf-3757-baa1-5f355b6a0cff | -4.15491 | -60.69982 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ed8ff8d-a26c-3137-9212-b8e443c9edf1 | -3.93694 | -59.33308 | 2026-08-29 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1c3b32d-ff36-3cde-bfe0-ae3a68aa15a9 | -5.22517 | -52.02075 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f982ac0-aa69-3948-8607-80aaf2ed7795 | -7.06359 | -42.15455 | 2026-08-29 04:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2bcd5e2-d968-3460-bddd-fa1d90cc00fb | -3.53421 | -59.02587 | 2026-08-29 04:51:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad89d68c-e03c-3cf6-8675-1bdd474b9704 | -2.98079 | -48.74391 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d39a4a43-0807-3f38-a12c-b78a5ec41f2c | -4.84572 | -45.39906 | 2026-08-29 04:51:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 495f7599-f70b-326f-864d-44a2d30d0985 | -5.25721 | -50.96472 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5f20ad5-b2cc-35ae-a6f7-4baeb573b9f5 | -5.33944 | -45.15939 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a4ffa844-c239-3123-b6f1-6123f556ecbf | -5.26052 | -50.96524 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8859a7a-aafc-317a-ae3f-ed6c3145c354 | -3.15902 | -54.62327 | 2026-08-29 04:51:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d12e531e-af6a-3e8f-ad8b-e3ad0b10c760 | -5.31347 | -47.04572 | 2026-08-29 04:51:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6a035f1-bd5e-322c-9f8f-8187081bcb75 | -3.15825 | -54.62803 | 2026-08-29 04:51:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8642a57-9dc6-3868-b5eb-8240d6c6cc7b | -4.05864 | -56.29065 | 2026-08-29 04:51:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14e05b91-f886-35a5-b4e7-b9b389d01ca2 | -3.21898 | -48.8103 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d39320-41fb-33b9-9d11-9dba4e902f46 | -3.75407 | -53.35825 | 2026-08-29 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9a7da52-7afe-3fd8-a724-047285147923 | -2.02847 | -48.77959 | 2026-08-29 04:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc730289-e55a-3911-a2bd-a989eb9fc28e | -3.93549 | -59.33228 | 2026-08-29 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbaa23ce-9e14-3201-9b17-a6e220e34174 | -6.62073 | -43.74742 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb81eda6-c22a-340b-8deb-52b8ed481d85 | -5.47485 | -45.1206 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5ee39c7-1247-33ee-a028-baad9e745042 | -2.49823 | -48.13598 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d69bdb7-5e8e-3fd5-8402-1607f88c1ffb | -7.07766 | -42.21184 | 2026-08-29 04:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b049833-c91f-3d32-8ebe-da3254dc859d | -2.02444 | -52.105 | 2026-08-29 04:51:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f241a4-10e0-3863-9766-d36a627630ec | -6.61594 | -43.74678 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7fef9f4c-494f-3be3-a62d-3c01c88f7740 | -6.6229 | -43.73178 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2951a28c-0f55-396e-a090-55c41cc2806c | -6.62624 | -43.74289 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b2e231e7-42a0-391c-8504-71ed1567643e | -3.729 | -58.99469 | 2026-08-29 04:51:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da935918-e8b1-3053-84d0-83111eee7539 | -2.72211 | -47.05489 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2683091e-a82c-3a2b-9ba6-5f52184221cd | -6.62696 | -43.73767 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6c10f012-19a6-37df-a38f-7e5e9c57bd30 | -4.5405 | -54.92535 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36aa25af-5474-39dc-900b-2ba76367a59b | -3.66474 | -49.18882 | 2026-08-29 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e40cf5-1107-32df-8afd-ce1ad805f37c | -4.16899 | -42.43529 | 2026-08-29 04:51:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb3f7e15-ed60-357e-8ae8-6b72dfa029ed | -2.49884 | -48.13219 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5be82e35-ac50-35fb-bef2-b84cd23900f7 | -6.62552 | -43.74805 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| be6d6d99-1f43-3f6b-89b8-ae64ee5c7713 | -2.25395 | -49.52572 | 2026-08-29 04:51:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86bf65cb-bc14-3b65-b29d-4c416eaddee8 | -2.98967 | -48.9529 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e252bd1c-6d77-3d53-808a-90dc07647c0f | 2.41067 | -60.87904 | 2026-08-29 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36e6db7a-c12b-39d8-beca-45c8bc4a1268 | -5.31279 | -47.05024 | 2026-08-29 04:51:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e330d0-f99a-338b-b19c-71d7fbb1020f | -4.15619 | -60.69217 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3dd62a8-24fc-3384-90a1-9ebba88a31c3 | -4.1544 | -60.68695 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cb25d86-5acf-31aa-9b32-f6f34f924a4d | -6.34057 | -44.09116 | 2026-08-29 04:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f6ef342-7f8b-3d47-8537-2f137489b367 | -4.97218 | -56.29469 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f87b9ac8-f16c-3c96-acfb-c524137e0c24 | -6.62582 | -43.74637 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ffb49d68-1f88-3283-8fb8-b030bc1ae4ff | -6.62145 | -43.74224 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d1c86aff-2502-3dec-b6c3-3e599c4615cb | -4.33965 | -55.445 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cedbec47-6441-3766-85fb-ed73e694bc6b | -2.95235 | -43.2528 | 2026-08-29 04:51:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aeaf2499-f58b-3fca-a065-708958490020 | -1.25057 | -55.70563 | 2026-08-29 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48e486db-78c6-39d6-8be8-91de5a347736 | 0.1533 | -60.39683 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68d5d975-f425-325c-9fa5-1e6dc8e98952 | -7.07278 | -42.20759 | 2026-08-29 04:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 839a1f13-894f-3bfc-a11b-159b15d398b6 | -2.72212 | -48.80131 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README41.md)
