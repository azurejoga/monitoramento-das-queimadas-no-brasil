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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26ab3b3d-63a7-367b-b8ab-01eefd18f6c5 | -10.85576 | -46.5846 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca8547e6-b1ad-3994-8b4f-6a63de121a18 | -10.77944 | -55.68782 | 2025-10-02 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba791edc-7a9f-3cb9-97cf-aaa08513fff2 | -11.353 | -44.97203 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac35c8e5-20e2-3d25-b6cc-f7ebd888aa70 | -13.22251 | -48.44018 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e480e06-b737-3116-b12c-ed0216826143 | -15.86181 | -48.13317 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4df7494c-ba1b-35c9-a82e-13b326705e4e | -14.89549 | -48.32853 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc039247-267f-3aa3-8f23-8a3635754c43 | -14.90449 | -48.31004 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8646b4a3-98af-32b1-a645-45a2b615d71d | -10.82506 | -47.94839 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bf4c8f3-acec-38b1-81c6-05e39f49f40d | -13.33738 | -47.34418 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f1f5236-aed4-311d-8372-7238009a9096 | -15.27985 | -49.30784 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58314ada-7840-3e73-813b-f1b55285fa96 | -14.88578 | -48.33562 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d4d428f-fabb-38e7-be2a-84b5a4e11cbc | -11.09827 | -47.84642 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 456fb428-d95c-305c-880f-b2233211eea7 | -11.59528 | -45.05456 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fc9458e-8f7d-3659-bcc9-0e1bc5581e75 | -13.75791 | -47.96849 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6701d7f-9bf7-3558-88ea-701e4ff59605 | -11.61381 | -45.03196 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8154d20a-3477-3542-9a96-2e557a04cdab | -9.85199 | -44.60271 | 2025-10-02 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25b58ed5-3a8b-3176-8845-7d8e96b85fdc | -11.90754 | -47.88338 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d45f56fd-16b5-35b7-b1f8-39a49134ddd9 | -10.21239 | -48.20018 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf63363a-5bb8-3729-afb4-f8147433f601 | -13.69309 | -48.62951 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 551c219f-5981-3927-b148-5f365ff3d2d5 | -9.94421 | -43.7245 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a94a3867-dde0-35f3-9fc4-3ba9af58edfa | -10.69078 | -48.57712 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6496649-d586-312d-a289-0fa4f515e13c | -13.40401 | -47.79431 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 194af2f2-1a6a-363c-8d2b-a46eacef2029 | -11.53559 | -46.95462 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41e6a11f-004d-3520-8f02-2b8f524cfa7f | -11.42868 | -47.28867 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d256dc33-096c-39b6-b2f5-49e68e90873a | -15.29254 | -45.0884 | 2025-10-02 04:51:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a508e5e-24dc-3d42-9ee9-cf1ef453c7ec | -13.47536 | -47.25086 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9baf063-2652-3743-864a-b0a33b021009 | -15.6469 | -49.25603 | 2025-10-02 04:51:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6c8c83b-3c43-3859-8fd3-4d700d636da4 | -10.21948 | -48.20866 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f562012-b4c7-3b16-9703-9a0ddcc22625 | -14.69224 | -48.10846 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b358d09e-0323-30a7-ac25-4c39b8d2b22f | -9.94874 | -43.68892 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b64a2458-4ffc-3e36-a4ec-9fd72e55152e | -12.22618 | -43.76715 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de8a6a18-bca1-3e69-a166-747aaefd2139 | -12.6734 | -48.57763 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 40993fe2-dad5-3ec2-b5d2-2848bfebac98 | -14.28377 | -45.97923 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14fff0b6-d625-3ff0-9188-1f2211fecffb | -11.46258 | -44.96799 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18bed7b9-7c2c-3668-841d-1610bf646b3f | -10.19315 | -50.2785 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffe681b5-dc56-3b77-9d67-6586f8ae0676 | -12.68516 | -48.55323 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9efb508f-2e7f-3ec6-945d-cea59d778958 | -14.83298 | -54.78102 | 2025-10-02 04:51:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 334bed79-3479-395e-8d9c-6a2a87a81ad3 | -15.25592 | -47.90705 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f3b40a81-8909-38fb-a247-4fb5dfe382ca | -11.02171 | -49.82201 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1da48159-e84f-3d92-8f1d-0ed7164027d3 | -11.92934 | -47.8824 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e75cce74-4b57-3ee2-9fa3-9b3416f6dc77 | -10.65904 | -48.49979 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f8b7c2f6-66e2-3f9b-8b7b-a51509430537 | -11.18659 | -47.18978 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9f94b6f-bdf7-33ec-8c22-3be8a7d773c7 | -10.70274 | -48.57895 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8817823e-97b1-35a0-9097-7df46e33be0b | -12.81397 | -47.02306 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f8a841a-7f90-36cc-b0b4-b69d4b7dbcbc | -15.31888 | -46.29355 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca1da909-4ee2-3668-987b-04e10edaeb65 | -11.46354 | -45.02523 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fc0ce5d-9698-3d37-ae1d-5c39f43f0eaa | -10.44832 | -48.08607 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0a8ad47-d086-395a-8868-ae4a6e70bec0 | -12.11343 | -43.43729 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfa84175-8f65-3c20-a77c-153c59750ff9 | -16.06287 | -51.00499 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca9d7973-bfc7-3c83-b593-6119413b05e0 | -11.87539 | -49.91143 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dbe19e0-1709-3464-bd9f-9a126cfa782d | -9.93234 | -43.73015 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bd0ce793-7f10-3949-a771-8f627404d41d | -15.23314 | -48.73005 | 2025-10-02 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab9e43bc-18fb-3267-b701-63f99ddf9765 | -9.89642 | -45.94577 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba7be6a2-a73d-336f-9a4d-fb948dd32ab0 | -11.46396 | -45.02205 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1575baf6-af94-3fb7-8784-9139e1d63665 | -11.46547 | -44.97109 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e94c7099-0831-3b54-904b-86a7b12c5bd5 | -13.31323 | -47.202 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 325669e4-e928-30c7-bd8c-27200ec64844 | -14.31243 | -45.99427 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d14653a1-332c-353d-ac40-73af7342957b | -14.98411 | -46.92331 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef840806-6a46-3b47-abb2-2b53587d318e | -14.08739 | -46.65636 | 2025-10-02 04:51:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08bd7aac-a149-3663-ab97-1f31a89b5434 | -11.20425 | -47.19199 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed31b613-9255-3eed-a4e0-2a6cf7dce0b1 | -13.75983 | -48.69725 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4db503e-ca77-340c-8765-60ced5d86770 | -15.25541 | -49.30511 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11e43639-71a4-3955-9011-45ca06740595 | -10.79901 | -45.34643 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 735a3973-a0e3-3bf4-a4b9-e1a3cd7764d2 | -10.99353 | -46.60226 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 5c010744-6bdf-38b0-b0a2-783d7268f79c | -11.52021 | -43.54634 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89764030-f72e-322b-955c-44b4b1474ef6 | -10.2314 | -50.31828 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ea0678e4-81d5-353d-b9c7-944077e98256 | -11.62113 | -45.05642 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 028e8c50-703a-3662-aab6-2c818850f988 | -9.92818 | -43.71894 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b5d48b4-d351-3cf2-95a7-44e7663a4401 | -15.34919 | -47.07153 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85a34a5b-f0ee-3efd-9d68-092196505906 | -12.2032 | -47.79493 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92418c10-bea9-304e-914a-5dc2f2491148 | -13.32554 | -47.80847 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbfeef31-8b6b-34fb-b22f-6bcd3a37dcee | -14.59063 | -46.71984 | 2025-10-02 04:51:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b2bd64d3-710a-3dcd-af05-08c539f521bc | -11.09093 | -47.83722 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c399dea-007e-3037-b693-9a3979b04220 | -9.93377 | -43.76271 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9dd89ba1-8623-38ef-acd8-e0ba10c5dc80 | -11.79759 | -44.97768 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 032c7936-6dfa-32ca-b612-7a9a7ca01554 | -10.22422 | -50.3172 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9622e4c-520c-3a8b-b390-431322c9ac2f | -10.01821 | -55.41241 | 2025-10-02 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4943dfd-eac8-3dd0-a28f-54da1bc802d3 | -13.31671 | -47.00029 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b50747c-462e-38bc-aaf0-2d9e559905b5 | -13.75627 | -48.69251 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e85ffa87-9902-3617-8c93-870518ec05d4 | -10.67784 | -48.58237 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e24ba11-b23d-3875-b0ce-3fc640170af4 | -13.01623 | -45.21245 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e52b8f7-dbb8-309d-bbf2-898e748ca693 | -10.22663 | -48.21667 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 014a8877-52b4-3271-8fc2-474a50882acb | -14.21227 | -46.11009 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0410c8ed-0d4c-30e1-8829-babbe5586fe6 | -13.00311 | -45.23322 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 390a55ff-82b0-3364-ab71-6b6b72e737fa | -13.21419 | -48.43888 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f7832ab-009e-3d77-b320-f530dd303105 | -10.77409 | -46.60152 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90e771f8-fdfb-399b-93be-bb1e58459316 | -13.57021 | -47.27485 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52b45508-d861-3935-8197-515f2a9eb70a | -13.36015 | -48.12368 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31069f6a-9e9f-3dea-9a33-9aec875943a3 | -9.94007 | -43.71321 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b888126-ee45-36c6-b8e0-bf0ec9188b3d | -15.25092 | -47.91067 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a6de0c3-4842-3b9c-936d-734c0c5af2bc | -14.47138 | -48.4367 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d675131c-e841-33bf-9a4d-07e6d9df7782 | -10.16631 | -45.46239 | 2025-10-02 04:51:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e0c2524e-1b74-3d08-9b3e-b8792b32fc41 | -14.86601 | -48.28657 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba282ebc-9bcd-3ebd-933f-cc5328fb6ed6 | -14.31748 | -45.99409 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8bab9fba-7db6-3e24-9869-bd5072c9c339 | -11.81629 | -44.91197 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e099401f-69f8-32ff-a693-0a6afcfe538a | -13.75255 | -47.99587 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a10f8b87-c17f-3a49-ae81-a2713e28ead3 | -12.67224 | -46.86187 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c55ec1d7-2a11-3a5a-a698-da8e926a0df9 | -13.32543 | -47.87476 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c071e6e-736e-3577-9380-5f0f26bd1e8e | -15.29736 | -46.38822 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 437cc169-adc3-3abc-9542-f1027bbb2283 | -13.77463 | -48.04345 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README122.md)
