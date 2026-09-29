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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2865fa69-83aa-3893-ad8b-7aa181b0e892 | -13.1992 | -48.5603 | 2026-09-29 12:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c8e2cf9a-0d2c-3aa8-88b3-270da98d0522 | -11.1962 | -44.8037 | 2026-09-29 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ab72eb7b-952e-36e0-8198-ab708befc1aa | -12.6467 | -47.2373 | 2026-09-29 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 028ff0a8-fd90-32a7-ba0c-c7d8b8da83e1 | -11.0544 | -47.6733 | 2026-09-29 12:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2249e3f2-b1cc-32c0-9564-bc311764f92b | -11.4495 | -43.4566 | 2026-09-29 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7a20dc1f-8752-3642-81e7-f559593e4dcf | -11.8678 | -50.4504 | 2026-09-29 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 32d10e10-d3eb-328c-a0ca-93c19a49a19a | -11.4307 | -43.4358 | 2026-09-29 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 6bcb2d60-48ca-373a-8e51-dd2ae8e4d2d2 | -11.8675 | -50.4718 | 2026-09-29 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e6720596-55db-3cd8-8ac1-96d041d8b5c4 | -12.6267 | -47.2851 | 2026-09-29 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e6c587c3-0359-38c0-ab46-5e6f90015775 | -6.914 | -43.6816 | 2026-09-29 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 61688ab1-f02e-3ccd-84d6-b5a27a6f44f3 | -7.506 | -44.5503 | 2026-09-29 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d67dd982-d443-38cf-87c7-64637d389325 | -10.2843 | -44.6274 | 2026-09-29 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2f3df763-0a59-3f70-bd47-4b4e04b80c1c | -11.4302 | -43.4596 | 2026-09-29 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| d8812e79-62e3-3c0a-9565-a513733c178b | -11.1907 | -45.1274 | 2026-09-29 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 59bc4ba9-6c70-3fa6-9432-25de3de144c3 | -8.0355 | -42.866 | 2026-09-29 12:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 7ff0a073-e636-3913-a5d2-229ca016ccc1 | -10.3894 | -61.2502 | 2026-09-29 12:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 0822e5d1-d424-3b4a-a178-fa3aebe008bb | -7.064 | -42.0648 | 2026-09-29 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 2807d68b-43bd-3971-8059-0a540cb49416 | -14.1115 | -46.2834 | 2026-09-29 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 4ead78e3-8115-3dfa-9540-fc8fd1d7cf99 | -7.3965 | -42.6498 | 2026-09-29 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 6d19e53a-5286-3dbd-8d01-f612ab405e4d | -11.1775 | -44.7832 | 2026-09-29 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 339.6 |
| 8bb39a5b-02be-332c-af6e-ea4d729697a7 | -9.4702 | -45.8023 | 2026-09-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| f845fdfe-2a86-3570-8b32-c4ac3947dea6 | -12.761 | -47.2881 | 2026-09-29 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 58b6a1b6-5a29-3480-a607-7eb69a7e6098 | -12.666 | -47.2345 | 2026-09-29 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2942beff-6986-37f7-9d54-63c3490cee08 | -14.5168 | -48.2958 | 2026-09-29 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3f31de2d-242a-30a7-a04c-6ea13a23a75c | -14.1309 | -46.2801 | 2026-09-29 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 42148682-59d0-3598-951c-84cd5ccc4093 | -12.7421 | -47.2684 | 2026-09-29 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| f1892919-7bf1-34fa-b6a8-4ab3911fafa8 | -12.024 | -47.8148 | 2026-09-29 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 161fee86-f5a9-3e90-81e7-2bd4e8cab7ec | -13.6762 | -45.7822 | 2026-09-29 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 28139e94-6111-3fda-81b6-fef07f28dde8 | -18.1144 | -44.3988 | 2026-09-29 12:50:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 60a597f3-a3e6-303d-9ccb-e3a3cfce5ac3 | -1.10862 | -63.12089 | 2026-09-29 12:59:00 | TERRA_M-T | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58229131-fc68-3696-9aa7-7729d17d8da9 | -0.99418 | -62.68973 | 2026-09-29 12:59:00 | TERRA_M-T | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87023a08-8300-30ee-9b9e-884326a10912 | 1.69378 | -55.95101 | 2026-09-29 12:59:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0f0d9174-2ee0-304f-8b54-0b9c9f80d85c | 2.79334 | -60.00369 | 2026-09-29 12:59:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| e54d453a-c8f3-3645-8e9a-ebbd9900dcab | 1.68874 | -55.91816 | 2026-09-29 12:59:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 27e741ef-8494-391d-ab7b-86ef636b79b2 | -11.8866 | -50.4696 | 2026-09-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 642c3d4f-e512-3db8-a0d5-4b490c90eea2 | -8.6451 | -45.3489 | 2026-09-29 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 56c7d021-499e-33ad-abf8-bdec6c47184f | -11.1962 | -44.8037 | 2026-09-29 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 7a0ed180-16d3-333a-bee4-de82f6e9e4d4 | -11.8675 | -50.4718 | 2026-09-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 917afb32-d30f-368c-8fa3-a42a26328037 | -15.3998 | -47.9261 | 2026-09-29 13:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f066afae-4afa-3618-bef1-084339caff6e | -12.761 | -47.2881 | 2026-09-29 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 111fe4b0-f2a0-3798-88fb-062e4bdc7436 | -11.1907 | -45.1274 | 2026-09-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 306.1 |
| 4a2f859c-74f1-3b4e-92d7-a2b39d377eaf | -8.2291 | -45.4602 | 2026-09-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 24c39fe2-daf5-3828-8af5-498e098ac626 | -7.506 | -44.5503 | 2026-09-29 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| bd577764-f657-32ad-acee-b08b5b7d20fd | -11.8678 | -50.4504 | 2026-09-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 2530ea9c-cfa1-3a67-8fd0-b2b2c74b52a3 | -12.4051 | -50.2139 | 2026-09-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b0173c2b-b7b1-325c-96f7-b4ab608d86a4 | -10.3895 | -61.231 | 2026-09-29 13:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| fbe4795d-b540-363d-92ec-49cb065fbeab | -10.2843 | -44.6274 | 2026-09-29 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a8516255-b327-30c5-b9e5-111c44479582 | -11.9183 | -50.8933 | 2026-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| db173cbe-6a67-30fd-8d01-b1fe95c10699 | -9.4702 | -45.8023 | 2026-09-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d8ed727d-54fc-3b60-aec8-8a63def729c2 | -9.1337 | -49.9656 | 2026-09-29 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fc3313ac-250c-3fbe-a07f-20ea215ac748 | -7.064 | -42.0648 | 2026-09-29 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 86080d54-7dec-3c83-ada1-0aaffd3bf5e6 | -11.8989 | -50.9169 | 2026-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 12bd600b-e6dd-3ae4-a6a9-cd510a9205a8 | -13.6762 | -45.7822 | 2026-09-29 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 309.1 |
| 3d28a714-0ea2-3357-a12c-24dcb8f703d6 | -13.1799 | -48.5631 | 2026-09-29 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 807335b1-afb2-33ff-9c1a-90aafc5cce7e | -9.0977 | -46.8088 | 2026-09-29 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d047ceeb-d51c-3811-82f1-230a141173bd | -11.4791 | -49.743 | 2026-09-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| dc045b28-19c4-33cb-901e-e23cdf55c1ec | -12.7801 | -50.6619 | 2026-09-29 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 3f6e7679-f5e2-3915-8bc9-1cb3b0851da1 | -18.1144 | -44.3988 | 2026-09-29 13:00:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 930d5669-872b-30ab-9565-5d178bbf6d52 | -11.4307 | -43.4358 | 2026-09-29 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| aeaf46d2-794e-3a25-93c0-4511b0795c87 | -11.1903 | -45.1505 | 2026-09-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 989ad0a0-c4c7-3af6-80ad-916364841b3e | -6.3101 | -52.6184 | 2026-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| a270b12c-263e-3dbc-96ec-1d088944bea9 | -14.1309 | -46.2801 | 2026-09-29 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e0bfddb8-9ef9-33cc-8629-ca663c02d6c5 | -11.1583 | -44.7859 | 2026-09-29 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| b55a19ea-bd25-3a13-a527-67e71d0dbbc7 | -8.2293 | -45.4375 | 2026-09-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 46d85a1a-6590-3a31-9964-cd0ef087f894 | -11.4302 | -43.4596 | 2026-09-29 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 3a2f955f-386c-3d1a-b689-c102c6cd1c1f | -11.1771 | -44.8064 | 2026-09-29 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 530.2 |
| 2d37e4f6-eec4-3ff9-ae0e-0350de307d10 | -11.1775 | -44.7832 | 2026-09-29 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 507.8 |
| c30ccc62-0574-3eb7-81df-81663b4dc33f | -11.1966 | -44.7805 | 2026-09-29 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 38be4c14-0e57-3111-9bcf-fe520ffea66e | -11.4495 | -43.4566 | 2026-09-29 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 8f066fe3-de9c-3693-b038-860e6a190041 | -10.3894 | -61.2502 | 2026-09-29 13:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 208.7 |
| fab04cab-4b65-39a2-a733-17ede595b661 | -12.386 | -50.2163 | 2026-09-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2363fe70-9fb5-3f8d-800f-4d0b4863434f | -12.7421 | -47.2684 | 2026-09-29 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1d864455-4a18-3914-8283-4634ae038525 | -11.8799 | -50.9191 | 2026-09-29 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8de2930b-8c27-3494-a8ed-86dff8dae988 | -13.1996 | -48.5382 | 2026-09-29 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e4113b36-305c-3e44-9afa-ba099b6e72c9 | -12.7798 | -50.6834 | 2026-09-29 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 391afed1-6219-3735-ad17-0ec74814ed06 | -13.1992 | -48.5603 | 2026-09-29 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 6e7eacdd-dab1-3a25-916a-6954e6da3575 | -7.86861 | -61.17759 | 2026-09-29 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c70abe93-7d16-3735-9f45-9c18734ad91d | -10.39347 | -61.26258 | 2026-09-29 13:01:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0345bcb8-31e0-3c66-ad43-b505af0dcb87 | -10.38325 | -61.2403 | 2026-09-29 13:01:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 8ad9d76d-4275-33bb-ba8f-4e2670703e3f | -9.10543 | -68.20302 | 2026-09-29 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 5ab845dc-2cee-394e-a1d7-ebe63e2fcae1 | -10.39601 | -61.24168 | 2026-09-29 13:01:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 235.2 |
| 29ce36a2-057b-3fc7-affd-1c29025d30e0 | -9.82588 | -64.97236 | 2026-09-29 13:01:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.9 |
| c637ad56-647e-3259-b26f-a13261f3433f | -9.122 | -67.83926 | 2026-09-29 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07cd0e08-51db-3a14-829d-9fe776f9b1ed | -9.19916 | -67.74126 | 2026-09-29 13:01:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b8763a8-1a93-3c46-9712-846dba214e4b | -9.45946 | -67.14828 | 2026-09-29 13:01:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 14f66d27-1a54-319a-abe5-3780be0eb48a | -11.83424 | -64.93546 | 2026-09-29 13:04:00 | TERRA_M-T | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 4d524b63-4793-34b0-b6f3-60ae12de252b | -13.6762 | -45.7822 | 2026-09-29 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 354917c0-b210-3c11-aede-6499d0158f27 | -11.8665 | -50.5362 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| dd9a719d-7210-3cd3-a63e-544a61a0f59f | -9.0977 | -46.8088 | 2026-09-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 02816926-2cf3-3683-b92a-3cb33bbd8ee8 | -12.386 | -50.2163 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b4189fc4-bab1-3833-94d3-c91af4cb2c1b | -12.374 | -46.3972 | 2026-09-29 13:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 3684364b-9ea3-3162-b8e8-2eab4bd88684 | -11.8678 | -50.4504 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| f0c4cd76-f632-3ce6-81b2-9143aefcb98f | -7.5245 | -44.5715 | 2026-09-29 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1f9a2d33-ba34-3ccb-be77-3669bd28f8bb | -12.7417 | -47.2909 | 2026-09-29 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b2f66bb4-1821-3494-a890-d58d25f52d3c | -11.8856 | -50.534 | 2026-09-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2ce9e140-6593-3339-a283-fad3512efce4 | -7.5057 | -44.5733 | 2026-09-29 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 7d86376c-4624-3c2a-b41a-9e5f8d1c8408 | -14.1115 | -46.2834 | 2026-09-29 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 25f29b4c-66dd-363e-8f78-909a2d74538d | -10.1098 | -50.1921 | 2026-09-29 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 38614458-366e-303d-a164-8017f21489d4 | -12.024 | -47.8148 | 2026-09-29 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 5959a518-9024-35f1-96f1-8f0290aa65e2 | -11.4115 | -43.4388 | 2026-09-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |


[Clique aqui para ver as próximas entradas](README76.md)
