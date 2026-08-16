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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40903934-e6e3-380f-a6d9-b19ede249e7f | -2.77084 | -48.57283 | 2026-08-16 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a6fd175-f223-3ea7-af7c-059f93724bea | 0.4939 | -60.59312 | 2026-08-16 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe7e9f35-0359-3659-ab28-9d4b29318bf3 | -3.96124 | -49.43767 | 2026-08-16 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76218387-ad96-3139-a41e-1d285215cc81 | -4.01409 | -49.46635 | 2026-08-16 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b188fe4-98c8-32a5-a518-442e16db7829 | -4.10804 | -42.50054 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a8965a26-70a5-37aa-9ffd-8df412f5d6a3 | -2.76635 | -48.57214 | 2026-08-16 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b60d21a8-7f41-3582-9139-a4e8b9205c37 | -4.0929 | -42.50556 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| aae6bba9-7258-396d-92af-07a92e48fd27 | -2.49949 | -56.05906 | 2026-08-16 05:14:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e1040bd-9f6e-310f-9e8d-07108830c3d0 | -2.74761 | -60.23908 | 2026-08-16 05:14:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b817128d-6838-3cbc-bb3f-61d0ffa3a3a4 | -2.50005 | -56.05554 | 2026-08-16 05:14:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c716f36c-4796-3976-b266-1c749b42dbd7 | -3.96064 | -49.44175 | 2026-08-16 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60f83d5-df6e-3668-b931-975fc1fb4e28 | -7.83796 | -61.35383 | 2026-08-16 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f712f0-5106-3dad-b2ec-821a484f0a69 | -6.96809 | -59.28584 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f2bf46d-ddd3-3488-823b-883e6564e71c | -6.09793 | -57.69665 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1abad0c-a3d6-3135-b3aa-9d0f6a6a045f | -10.52946 | -44.8497 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4f27b8d-7f00-3d89-bc0b-c57c5aabfb83 | -8.64128 | -54.69264 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7efce02f-e74c-385e-b737-0bde04cc0a41 | -6.84254 | -56.44733 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d9f743b-322d-36cd-8b1f-6f3c600e7440 | -6.37358 | -58.31799 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d7bbfbf-e7a7-3f6e-8c05-d295b40b9bbe | -6.82205 | -56.44763 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e95a987-955b-344c-8c3d-9b1fa6340696 | -6.70875 | -58.93598 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31719575-b72f-3ed9-8482-fa3faf4f8f13 | -7.39043 | -59.99829 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f88303e-85ef-3816-b736-d1cc9257b6a4 | -6.81541 | -56.44658 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ad5a66e-9fe6-35ca-8404-ad378eb56dc8 | -6.85583 | -56.42805 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6f6394f-7272-3014-8a73-9f6d3888dd9b | -7.53452 | -55.58472 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a38fe4-373b-3a65-b78a-2d8c21c1a862 | -9.54161 | -56.79856 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dd39159-19e6-31a5-a791-39c86e856599 | -11.22526 | -54.8236 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d05f4bec-adf7-3e0b-a86f-3d49babb21e4 | -6.88182 | -58.94293 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f125d5a-7164-31c8-af3d-09b3429efc40 | -8.60205 | -54.69779 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d56f845-6960-33e0-a107-9a96c8d6896d | -11.45399 | -46.6092 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49b199c7-a82e-35bb-8af3-b45d4ef74f0d | -6.61422 | -59.05266 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c51fe5af-1857-386c-9289-cba987e416b0 | -12.44241 | -46.65767 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10bb6858-bcae-3049-af9b-0f8f95f06e78 | -9.10378 | -46.38617 | 2026-08-16 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddf099c5-9407-3aef-ac40-601e8d18bc5d | -6.83222 | -58.97664 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| efbcdc20-8f9e-3ce6-906e-9f3f21c8ef5c | -11.87385 | -51.94889 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 117d6f66-b45e-3207-a54e-00703dd96690 | -10.71823 | -52.1091 | 2026-08-16 05:16:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b262ed2b-5e70-3651-80f0-b4d469fc89e6 | -6.61787 | -58.98533 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e97aba8a-0c63-3ae2-8fd9-be494d238994 | -8.43877 | -62.67578 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7aa5e3bb-cc5f-3783-8bb1-54b80b242961 | -6.70808 | -58.94005 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9ddc84a9-3e36-3470-88b8-e63f86d2e94c | -6.63177 | -59.08125 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dac4b282-4f21-3f50-808d-ed5ad3838f54 | -9.47603 | -60.52325 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ea434cd-dcf1-39d3-a3f1-2d8c42d718eb | -8.42565 | -62.67344 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b296b8fe-167d-36d5-80eb-61717cd66667 | -6.86922 | -56.40519 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc2e6543-6a8e-3c63-8deb-cdfb2fb7ddcf | -7.38966 | -60.00285 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d61f811-ad81-3b93-9d67-6c57a1d0ebb5 | -6.11385 | -57.70687 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3bdb051-a38f-3a9f-b41a-1c5436a1664e | -6.97799 | -56.46511 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2096fb9-d29d-35fb-bb99-035d49c2d671 | -6.83313 | -56.46365 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f98cb19-7036-37cb-9269-ee19a0297449 | -6.82925 | -56.44521 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35ca9f1e-9296-3599-90f5-fdbb9e631269 | -9.54493 | -56.7991 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 272d6ff5-51bf-3559-a1e6-7bd0af159319 | -8.26863 | -57.34948 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e524af2-a5d3-3396-9818-6698952a9454 | -11.22815 | -54.82801 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9a05ec8-3e0f-3b29-934c-fc5306bf911e | -7.4585 | -45.09892 | 2026-08-16 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 277b73ff-c5a5-3b82-bf33-fa6d31bab653 | -8.95672 | -60.57305 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 212e4892-1b48-3b9e-9f06-a80c20c0a647 | -7.42648 | -60.01346 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e677e1d-bdf7-335f-9ecc-ee06fcfccfe1 | -7.27324 | -44.71608 | 2026-08-16 05:16:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8d3d565-cb15-3787-9deb-51e874656f31 | -8.95752 | -60.56834 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c0efab9-e93f-3296-97ec-7b95e7156ca0 | -8.59864 | -54.67458 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b34211e-b008-38cb-8d84-52796a42a795 | -11.08381 | -47.25061 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 923cd750-c78d-37f3-8dd0-d20a8294e11b | -8.90115 | -60.57795 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 811d10a1-1032-30d3-bc42-4a825930fe32 | -6.60214 | -58.99121 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c3655a6-c07e-3a0f-a762-8e969a656cf5 | -11.45446 | -46.60545 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccef5d88-4fca-317b-b963-8dda1366c21c | -11.06902 | -47.27779 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d5ba9ce-123f-3aa2-b939-42c2bbc50286 | -8.95765 | -60.54445 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e687fec2-43e3-3d8c-a84f-6975d69be58f | -9.09753 | -46.38958 | 2026-08-16 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8369a11-dc87-3810-92a0-b00a8deeaeb4 | -8.97973 | -60.52906 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| acd136b6-fb87-3d97-807d-fbb10124d5ae | -3.50593 | -59.5823 | 2026-08-16 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cec52f6-1ab7-3afa-84ce-0268063691a9 | -3.50739 | -58.95136 | 2026-08-16 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a9fe175-c473-3f87-9254-c852c1498072 | -11.14208 | -49.03926 | 2026-08-16 05:16:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2818016-5874-3835-b97f-23228b4d436a | -6.9748 | -59.01587 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9773d161-3295-3de8-986c-d18cd6be5885 | -6.1155 | -57.71855 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ea8e019-bd5d-3aad-bc6c-1e7359261f53 | -6.69822 | -58.95512 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4b60d83-d341-3127-8389-b9f2b348566b | -6.6257 | -59.05033 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfb7a4ca-a539-31be-87db-c2499fd27042 | -7.39418 | -59.99892 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f953a4-8a97-30d5-b368-fd88f0386d99 | -8.64883 | -54.71225 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dda8c963-a6f0-346a-b06d-9ecd4fceddfb | -6.06816 | -57.70703 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72b68cc4-a3fe-311b-8213-40d25e0132d2 | -8.64527 | -54.68948 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c94fb604-7159-3bb7-8c1a-9faa5f030360 | -9.30269 | -56.80989 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9680a01f-ece5-394c-ab10-610a42565ef1 | -6.70316 | -58.94755 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdd3d4d2-f4bf-31e3-961b-99bbcf93df1b | -7.41222 | -60.00641 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59c0b765-436d-3d2e-9302-8e12bba50117 | -10.07985 | -60.49615 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e47c3b6f-fe37-3773-a886-969e0b633568 | -7.58776 | -60.89092 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cace89d-0d9e-332f-8f2f-5b9f7c5fcd12 | -8.96236 | -60.51653 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b96033a1-f125-3efa-b158-3a7dfa328e8f | -6.31304 | -43.62394 | 2026-08-16 05:16:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2b6ac6d2-9aa9-311b-94c9-2c5d25240211 | -6.7047 | -58.96048 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85d73aef-06e9-3ba9-82ca-250f60c8c036 | -8.42899 | -62.68008 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 81d72549-0bb9-33d9-9df5-32c956b1a2bf | -10.27142 | -48.28837 | 2026-08-16 05:16:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f79d6a2a-de09-3511-a131-0c726cd2711d | -6.82039 | -56.45807 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a6eddbd-09a7-3768-a506-b00cc4483bc7 | -8.95322 | -60.52451 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fede4dcb-9c50-3093-a808-127407914b3e | -9.46616 | -60.53569 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b38044e3-a148-3f0c-808e-2b64808d70cf | -6.53527 | -55.17669 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57e4a941-5484-3988-a52e-bc133efc7a35 | -8.89296 | -60.55737 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf250f99-d55f-30e0-ac41-9466a98bb3fb | -8.64696 | -54.70111 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80d60d82-1524-3180-837d-0d9a35c51eff | -7.34925 | -59.59782 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c6bf24c-862c-3ab5-8553-0b167c4e6693 | -8.61864 | -63.7251 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 277ab6c6-138f-3960-9e95-815892779b6c | -6.61855 | -58.9812 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba5ab1d4-fc84-3a06-85df-0187071a5ab0 | -8.43591 | -62.66649 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 32964bde-a229-30b9-af6c-29990f5d0435 | -6.84531 | -56.42994 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24f74474-7f76-35c6-91d2-c92168c54a3d | -11.21366 | -54.81807 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 039162b7-1783-3ba8-b203-1c45d023aeb9 | -8.97137 | -60.53241 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e2bdbdf-7fe7-3891-a212-8e729718e520 | -6.9689 | -59.30336 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac4dac72-8b40-3cff-b247-59f0c2c0c174 | -8.96159 | -60.52115 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |


[Clique aqui para ver as próximas entradas](README33.md)
