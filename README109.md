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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce31d704-357d-3bdd-ad09-0ba162f88519 | -11.5969 | -52.113 | 2025-09-04 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 180.2 |
| bab2c183-7118-3ac8-96bd-588c54bab80a | -5.6992 | -45.2692 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 9322ddc8-75ec-3ca0-8a9a-5989a0754242 | -12.4785 | -48.0859 | 2025-09-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3a09d0a2-f79a-39b3-bc09-0a55196f2840 | -11.9635 | -45.7741 | 2025-09-04 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d7203faf-5bc2-30c5-b81f-914f5e9ff45d | -8.02 | -44.084 | 2025-09-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 629fdb58-faff-36e7-a2d9-16204532f339 | -6.2315 | -42.4515 | 2025-09-04 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 232.5 |
| 84803420-631e-32e0-ba58-bf6315da45b6 | -5.7002 | -45.156 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| d14c8a2f-8983-3bb8-8943-d074f4129f26 | -13.8651 | -47.9734 | 2025-09-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b7802dd5-f2b3-3c47-9158-40b06c89c672 | -12.5233 | -53.8071 | 2025-09-04 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 71cf204d-2ef1-33bc-9b3a-cbfdd4ace2ea | -14.5852 | -53.0268 | 2025-09-04 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 955f0aa2-d209-3d37-8220-72539b53b423 | -8.3644 | -48.3116 | 2025-09-04 14:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8be9fd31-5b26-396c-abd8-cca681b18f55 | -7.0131 | -43.2291 | 2025-09-04 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 94306711-38c3-3300-ae96-5b5ba199d68d | -6.8941 | -45.5609 | 2025-09-04 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 277.3 |
| ef67c604-6c62-369c-a95e-ae1cafe0967e | -6.7686 | -45.0051 | 2025-09-04 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 68b2cc9e-2206-3065-a147-8896145282e2 | -6.8944 | -45.5383 | 2025-09-04 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 7194eb01-f614-3758-9bfb-4d5489dd6d4e | -7.7066 | -50.3188 | 2025-09-04 14:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e4576a38-9d95-353e-96ce-6b020f7912d4 | -13.8647 | -47.9958 | 2025-09-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 884f767f-3816-3289-a994-2c9cacaeb631 | -8.0796 | -45.3617 | 2025-09-04 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 58cbdc77-4382-3f0c-94e0-dd0a776d5d53 | -6.2606 | -43.2961 | 2025-09-04 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| bf06a490-0dcf-3556-a56a-58316d6cad67 | -5.6981 | -45.4048 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5c98daf6-19ac-391d-821a-bcdf47702ed3 | -4.8862 | -41.771 | 2025-09-04 14:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 192.1 |
| cebfade7-2493-3db2-93c9-6bca5d915eae | -11.0062 | -45.9072 | 2025-09-04 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 5210bca4-6b7d-3291-822e-d112f9af8ffd | -5.8292 | -45.3729 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 864f9a00-1337-3beb-96bf-9a332fe72838 | -11.3893 | -43.6075 | 2025-09-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b9ebcab9-abad-3818-8c22-e0298b354aaf | -11.5782 | -52.094 | 2025-09-04 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 217.1 |
| a56197ef-39d8-3a39-b156-6ca0dc0bd912 | -10.1457 | -46.2424 | 2025-09-04 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6d17de43-abaa-3c8d-8351-841a9e98aea1 | -7.6854 | -48.717 | 2025-09-04 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c72a7fda-b6da-3c6f-8ed6-b5721297283e | -5.6963 | -45.6076 | 2025-09-04 14:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| aab9436b-fb47-3ddd-a74d-60ef7d0d8ac3 | -10.4655 | -50.412 | 2025-09-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| c9869a86-ec9c-3816-a670-864a621dc385 | -7.0128 | -43.2525 | 2025-09-04 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 21d36774-bd7d-3cb4-85c2-fcc60743bc97 | -8.0389 | -44.082 | 2025-09-04 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 0383f706-8334-3afa-87cb-53c2d198c7ce | -5.7179 | -45.2679 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| ceaa1ad1-c373-3392-b22c-6d4a0642bc85 | -6.2205 | -43.5558 | 2025-09-04 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 95191edc-aeeb-321d-a6f3-e5ad0ec0fb52 | -8.0417 | -45.3882 | 2025-09-04 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f758b4bf-914e-3c83-8bb6-b546ec51f0dc | -7.7036 | -48.7587 | 2025-09-04 14:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 94408fea-cb0f-3bd3-acad-b8e793913c38 | -11.2005 | -55.0195 | 2025-09-04 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 3efb7118-ed16-3199-8b31-e4079c411bfc | -4.9049 | -41.7696 | 2025-09-04 14:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| c8a2d43c-c1e0-3f3b-97bb-83c43f800f99 | -12.5173 | -48.0584 | 2025-09-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7b7b1a0e-1928-33ef-8de6-86e92e379ed8 | -8.0985 | -45.3598 | 2025-09-04 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 2322b8ec-18df-3b71-a0a8-09bcf35bfdce | -11.7385 | -47.7637 | 2025-09-04 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 97f3b72d-6cdc-3cec-a05d-b8cbb5cecdf5 | -11.6601 | -54.5093 | 2025-09-04 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| dba4a7cf-6ef2-38aa-9eb4-fe150d616952 | -16.5497 | -55.0991 | 2025-09-04 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| d27c1fd1-b862-338e-8609-50116871df7f | -9.6848 | -51.0397 | 2025-09-04 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9770afae-21ce-3923-8ecd-1ad01df9f0bd | -6.8466 | -52.8132 | 2025-09-04 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| da542bae-01f7-3641-ae4a-e99c8d573fc2 | -7.0502 | -43.2724 | 2025-09-04 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 744c223f-9e36-3ab1-b89a-dfccc7afbb5c | -10.4658 | -50.3907 | 2025-09-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0ad5aa55-370d-301a-a596-df33dfbcc526 | -6.2952 | -43.5961 | 2025-09-04 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b6187a62-3493-304d-812c-a53f2499d9ef | -12.4597 | -48.0663 | 2025-09-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4cff6bf6-0af4-3709-8621-83b0f9a33a5f | -5.1191 | -43.0795 | 2025-09-04 14:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d13fd257-f3f1-31a6-a9b3-1e9cb4ae8234 | -15.737 | -53.635 | 2025-09-04 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| aeafadba-5c7c-381f-89f8-86c03a3ff877 | -8.2001 | -49.5988 | 2025-09-04 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f1b77356-9d59-355d-9ff8-ca8df684c05a | -11.853 | -51.453 | 2025-09-04 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 152.2 |
| d06cfc45-d689-344f-8992-9bbacf5067f9 | -8.0203 | -44.0608 | 2025-09-04 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 14b6aa4a-ba51-3a8a-82b0-e8529d18d31c | -5.7 | -45.1786 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 2fa30b8e-bd85-35af-b588-3975e63bb00f | -15.4564 | -53.0183 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 14355ae4-ee25-32ba-b511-ad273579fcb4 | -5.6777 | -45.6089 | 2025-09-04 14:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 6b2b7ddf-b7a2-377b-b237-b87d8c8309a1 | -5.7187 | -45.1773 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ae95eca5-2a1a-337f-bb94-87261ec38f8b | -6.0419 | -46.6771 | 2025-09-04 14:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 4d2817c6-0b91-3db9-9957-063e83442e67 | -11.6525 | -52.212 | 2025-09-04 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 6752ee7e-8031-34a0-bd49-7840f1a92a64 | -4.9951 | -56.256 | 2025-09-04 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| d6df9814-bb7d-3489-a3b7-ba85992608a2 | -6.2062 | -45.0506 | 2025-09-04 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fc0addb3-682e-3b98-a3e2-f1d5ad10179e | -8.2004 | -49.5773 | 2025-09-04 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ab81061c-7d60-3811-86b5-8717cb9ed96a | -5.8206 | -46.3595 | 2025-09-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| d219a27a-29cf-311d-acf8-9840e4b060e9 | -8.0799 | -45.339 | 2025-09-04 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| f8e36664-d244-3d33-ad3b-f2e0df8d6b6b | -11.5972 | -52.092 | 2025-09-04 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 153.2 |
| da183c7c-1e66-3aaa-a761-6ddf8314294a | -11.0044 | -49.7541 | 2025-09-04 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f1d779b5-e83b-3f97-8fac-44893e39fbd5 | -11.5963 | -52.155 | 2025-09-04 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 995307a3-ad57-36af-9b10-c0e8c36f595e | -7.6851 | -48.7386 | 2025-09-04 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 219.2 |
| 7c7b4cfc-8666-34ae-be4d-1d7d7117bbd6 | -11.3897 | -43.5839 | 2025-09-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 9cd31f9a-acb1-352c-aada-5318cec94a1c | -13.8457 | -47.9764 | 2025-09-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c0404b1b-61ef-3a72-91ee-1068b5f17891 | -11.8533 | -51.4318 | 2025-09-04 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6d4cf493-7570-385c-8442-5739e00b1226 | -7.2898 | -43.7162 | 2025-09-04 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| a57e1641-0e28-3c54-9d58-69d9431f89bb | -6.1667 | -43.3039 | 2025-09-04 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 931c3d49-761c-3ba5-a719-97937f0d9513 | -7.9117 | -45.242 | 2025-09-04 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9d3fb68a-1835-3a67-bebe-a341572e7b83 | -15.0449 | -50.068 | 2025-09-04 14:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 8016d4dd-95bf-3c00-bf9c-4ca2d2408b2d | -12.4981 | -48.061 | 2025-09-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f856cd38-c256-3579-b32a-0eb2de3c3df3 | -11.8343 | -51.4339 | 2025-09-04 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9c292903-38f5-38ed-b99e-c8974e621155 | -12.523 | -53.8278 | 2025-09-04 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8007dba3-08b5-3172-99d6-480e806cb150 | -6.2318 | -42.4278 | 2025-09-04 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 165.7 |
| adaa33a4-2a8a-3030-a934-4536a97b608b | -5.7341 | -45.56 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2f195ae0-507f-3041-b8c5-3919f07087a1 | -10.9867 | -45.9325 | 2025-09-04 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 33561b54-014f-3a2e-a763-c0c3fc933f4a | -6.0421 | -46.6549 | 2025-09-04 14:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e237e36b-c367-3c94-b055-9ca4226fa66c | -5.7528 | -45.5587 | 2025-09-04 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 2d40c2e1-9aaa-3489-9dc1-b7124129faf7 | -5.8525 | -57.7722 | 2025-09-04 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| f7025e67-c7df-35f1-951c-ff3860c0c79e | -13.8453 | -47.9988 | 2025-09-04 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ab036aef-24ba-3f7e-ac01-58fd423f24ce | -5.6815 | -45.1573 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1e2c20a0-a322-30c6-8c25-dec73c16d969 | -9.5023 | -57.8229 | 2025-09-04 14:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ee6d4043-17a4-3246-a115-f65b76c36ecf | -10.5316 | -57.7747 | 2025-09-04 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 4be9f539-e9e4-36bf-8d79-4490dbb20fb5 | -7.953 | -44.9417 | 2025-09-04 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7602b600-689b-3ba9-a12a-bace623d2c2d | -5.699 | -45.2918 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| fbe64e52-96de-3a30-9fbe-3d1499e28d53 | -11.6235 | -46.6388 | 2025-09-04 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c8d56f14-2268-3c88-8511-040174bfe4f4 | -11.3901 | -43.5602 | 2025-09-04 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 02f67f21-eb7d-3f8b-96c0-94e3b8b6606a | -12.9006 | -56.9488 | 2025-09-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| eafd7402-ff7f-3d37-aeb7-9428f82b0de4 | -13.1079 | -57.1109 | 2025-09-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c942f678-a5f0-3536-9e1d-a81c82a71091 | -15.229 | -52.7101 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 910a0041-1188-3531-a91c-17000d6aaa7e | -5.753 | -45.5362 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 431b157a-bd06-3421-99ab-f5609aafac5c | -6.0232 | -46.6784 | 2025-09-04 14:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 191.6 |
| a84afc35-5cf0-3418-9d41-2d78c8301199 | -17.0652 | -46.449 | 2025-09-04 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 106.6 |
| aeb4a7d9-9ac4-3f5d-9026-85f2ec3ef1eb | -6.2977 | -45.2702 | 2025-09-04 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 42dc7ba2-c142-37f2-a375-67622463b707 | -5.7177 | -45.2905 | 2025-09-04 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |


[Clique aqui para ver as próximas entradas](README110.md)
