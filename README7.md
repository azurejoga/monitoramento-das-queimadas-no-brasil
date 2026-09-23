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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fde782d-5a45-345d-ab74-5887a4cf355b | -2.54949 | -49.10283 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 43042eaa-2db1-38e1-b703-f324da715b02 | -1.14606 | -49.15148 | 2026-09-23 00:03:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53adc3f8-cefb-3f31-a18c-b90c565a6c47 | -4.45864 | -55.0732 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 2451350e-c23a-355e-b63f-10daae73e58c | -3.15813 | -57.68402 | 2026-09-23 00:03:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1de733fa-40f0-352d-9294-34b2726d43cc | -6.28516 | -52.95845 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3491770d-95ef-3cc8-ab63-da805a6d8194 | -4.0702 | -56.21886 | 2026-09-23 00:03:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8b3a24a0-a8d6-3f27-97f4-85904babff03 | -4.91372 | -45.65758 | 2026-09-23 00:03:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 429e3934-ee7e-3c64-a42c-6b12b9064f90 | -3.88128 | -51.95633 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0a07e41c-2fb5-3c85-8cb3-146e8403499d | -5.80306 | -49.16437 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3e6a2043-9049-3314-8b21-349c82cbb6dc | -2.85588 | -57.79155 | 2026-09-23 00:03:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 36d3e1cf-798e-3d92-a5ca-22eeb9c17ff7 | -3.50703 | -53.20055 | 2026-09-23 00:03:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0ea315e0-6a5b-3119-9c2e-2dfb85ff3071 | -5.5649 | -42.72119 | 2026-09-23 00:03:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 333a706f-33d9-340d-8a73-53a9328ad18a | -5.82922 | -49.95762 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f5ab988f-622a-38cf-bb4d-27a49cc2f7eb | -5.57636 | -42.73606 | 2026-09-23 00:03:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 78ba893e-0480-30c9-ba7d-b739e6e27ea7 | -2.30183 | -48.58361 | 2026-09-23 00:03:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 000f8e05-a9ae-34f4-b1ee-a4db50e67402 | -6.13014 | -51.70316 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7ffb424-c02f-39da-aec6-347c35c57419 | -4.91481 | -39.60825 | 2026-09-23 00:03:00 | TERRA_M-M | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 43.1 |
| d899233c-2e80-302e-8d99-05b33291f693 | -5.61248 | -45.95132 | 2026-09-23 00:03:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 579c6990-5617-3725-a841-3ec1247cc4ce | -5.86275 | -46.11634 | 2026-09-23 00:03:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 311e5100-55e0-3ddd-9785-6fecd29bca96 | -4.27978 | -48.61951 | 2026-09-23 00:03:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 624626e1-4ddb-38f1-a705-aba385dbc958 | -6.16723 | -52.05552 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17d611dd-9571-3f40-aaca-561e6a6935ea | -6.43159 | -48.44783 | 2026-09-23 00:03:00 | TERRA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b6d2ce24-b58c-38cc-8192-6d7c5b107871 | -3.49723 | -53.20189 | 2026-09-23 00:03:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e605db5-f7c8-3ed8-b7b0-b55233050cac | -2.96084 | -54.07681 | 2026-09-23 00:03:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9108e224-6059-3cd9-89e5-9062e1876a7a | -2.25206 | -48.75293 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d3c3ed51-b5ca-3469-91a5-a4799d33953f | -6.61231 | -59.95866 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| e3e398e0-8b4d-39c6-bc07-47329cbddafb | -6.17681 | -53.29897 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0509d263-ddcb-33b8-a99e-34d16e343e85 | -5.47565 | -48.86462 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7f5efe95-ef75-365a-8b1b-b3af1ab3e2d1 | -5.86815 | -52.0683 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6d39452a-a048-3406-8c69-bfb18d0239b3 | -1.41578 | -49.30362 | 2026-09-23 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f1e728a-9351-3d86-8574-844b4c4ae322 | -2.97508 | -50.39101 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 49b36ee0-884a-3d6d-8609-696927685a6f | -6.17521 | -53.28677 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5e95ab45-f385-3b81-903f-1a23b9ed4d8c | -6.18679 | -53.13942 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd1aae8c-d73a-3706-8d25-c01e38d5b8c9 | -6.1817 | -52.79184 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 16916e2a-ae75-3955-80f8-985a48aac0aa | -5.85317 | -52.02862 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 47a5c4c3-25f4-3cb9-ab9d-aeb1ee2036dd | -2.23243 | -48.74599 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc40c5a2-2a87-38b0-b769-97c795e14a44 | -3.62177 | -51.46997 | 2026-09-23 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| d80d53b7-d461-3436-b087-cb0f649ba44a | -5.62363 | -45.24807 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9a75a94b-1ad1-3797-85f9-18cd7ea329b4 | -5.76526 | -45.11284 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 415.1 |
| f823eafd-9b40-3703-a45c-99d64f1fbe97 | 2.93542 | -60.45445 | 2026-09-23 00:05:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4e89c761-e97e-3d63-a824-9772f94880ed | 1.78048 | -56.04902 | 2026-09-23 00:05:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4d899e94-d3c9-385c-a176-2276df5e8b0c | 1.43629 | -50.81646 | 2026-09-23 00:05:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 12e2dc3f-bef4-3ea6-996a-61601b4132c3 | 1.78258 | -56.03446 | 2026-09-23 00:05:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 8a7520b2-c739-3dc2-9c53-d2df96205476 | 2.91982 | -60.45206 | 2026-09-23 00:05:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| cae6af94-50e5-34d1-9811-9ba46e843a06 | 2.08136 | -50.94872 | 2026-09-23 00:05:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae85c4ea-6d81-3d24-8dfa-443dcb77f0e9 | 1.56612 | -55.85343 | 2026-09-23 00:05:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fe2bb64d-a723-3371-894d-de7480f636b2 | 2.93502 | -60.42951 | 2026-09-23 00:05:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| cfb5161b-2d06-3d15-88ae-ef7fd1b7ee96 | 1.43508 | -50.82525 | 2026-09-23 00:05:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 10ee80bd-58d3-305f-b8e5-c6cf4ac0ab26 | 2.33764 | -50.76904 | 2026-09-23 00:05:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 32a7c1fe-43c4-3715-b358-71aaec88e48d | 1.5621 | -55.88198 | 2026-09-23 00:05:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d5e62cfd-766f-3311-bd49-a72b6b311f74 | 1.40947 | -50.74998 | 2026-09-23 00:05:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 34a6b6ec-c611-3882-8dcf-88a7eb52e5eb | 1.40826 | -50.75878 | 2026-09-23 00:05:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2656687-f210-3b2f-9f5e-72ee8823a52d | 1.40064 | -50.74875 | 2026-09-23 00:05:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a75e0854-de47-31cd-9ede-23655270b044 | 1.27378 | -50.85318 | 2026-09-23 00:05:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 196d88e0-b1ee-320b-96a1-4b4461e48bf7 | 0.60505 | -55.9856 | 2026-09-23 00:05:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bc260c45-1597-3661-a026-c2224ee9412d | -5.3451 | -45.1803 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 515fe7d9-ef41-33c2-8a62-0ac45fef5315 | -8.8463 | -50.4804 | 2026-09-23 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 91631a9d-e0de-337c-a6f9-afe85a276dbe | -14.6302 | -45.6403 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| e88ad244-eeae-3415-be53-b18d32279c1e | -3.6763 | -60.5839 | 2026-09-23 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f5be8a83-59ec-3238-adfb-7fce723dcdfb | -7.0349 | -44.6625 | 2026-09-23 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 9e8fcfeb-7382-353e-ae4b-3259081ba8bf | -8.5171 | -57.6064 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 85318aa8-88ae-36fb-a75a-560aae98817e | -3.4598 | -59.5591 | 2026-09-23 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d7b8ee43-c933-3d90-8209-dd1adb14e1d6 | -3.6764 | -60.5649 | 2026-09-23 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 08336b32-8600-30e1-aeb7-527e6426f3f9 | -8.4726 | -48.6927 | 2026-09-23 00:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6b92e17b-2b13-335d-ba5e-f1094234946e | -5.7565 | -45.1293 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 20d40768-caa1-3b1e-a3e7-3d0e86681bfa | -8.9351 | -61.4759 | 2026-09-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f803cb2a-b23d-3036-8265-f311fc16a5af | -9.9625 | -48.4806 | 2026-09-23 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dcd92142-1452-3d54-81d5-68026283f67e | -6.9403 | -46.5426 | 2026-09-23 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ccba2305-f7f2-3bd6-ba8a-e5cf04f4d5b3 | -7.8811 | -61.1779 | 2026-09-23 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 5418d876-3594-35fb-b3eb-6f939340de67 | -14.748 | -45.5958 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 1a161c8f-ae9d-343e-82ba-b917007061a1 | -5.7752 | -45.128 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 02586c58-6b5b-3b3d-883e-c8b20d4d0827 | -4.0925 | -62.1062 | 2026-09-23 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 83e770e8-cea4-33fa-836b-c023ac1e7c42 | -10.6094 | -53.9902 | 2026-09-23 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| a02c9595-78b2-34b8-b195-0179814eb70c | -6.6775 | -58.5748 | 2026-09-23 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 86b7c542-6ae0-3ad8-9f15-96b1f349a671 | -9.1025 | -61.4299 | 2026-09-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| c64d13e4-f720-3339-8e83-1a72f75e854b | -4.4488 | -55.0662 | 2026-09-23 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3feb295a-33c0-36a5-99c4-68ab63ee87c7 | -3.2313 | -46.9596 | 2026-09-23 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| eb8c32c5-bc9a-37ec-871d-af53a18e140a | -6.9214 | -46.5663 | 2026-09-23 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 1be24540-6eb8-39c2-8a79-521dca00fad4 | -14.7279 | -45.6226 | 2026-09-23 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e7309445-d753-3e30-b968-d9e6ea62f51e | -12.478 | -47.0145 | 2026-09-23 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8ec80c32-8eb7-3754-a75b-1a7ebc2bd68e | -6.9216 | -46.5441 | 2026-09-23 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 0a65f18b-d33b-3f8a-82c7-56cb568471b9 | -6.1111 | -57.6645 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 68533310-c8cd-3bab-90c2-15ed65210165 | -9.1024 | -61.4491 | 2026-09-23 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 54a5904c-8b0f-3ee0-9141-5f3aa601f9d9 | -15.6574 | -43.527 | 2026-09-23 00:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1bd8ca9f-1461-3479-b318-0ad406a6bf8b | -10.5087 | -44.8748 | 2026-09-23 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 0497c854-a3b4-395e-9ccf-dea586e661a3 | -6.1109 | -57.684 | 2026-09-23 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 84bf67c6-476d-33b1-b7f0-fce5589c00b7 | -3.2314 | -46.9376 | 2026-09-23 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 9184f88d-18bf-3535-906c-293d4976ba69 | -7.0352 | -44.6396 | 2026-09-23 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a4656bc0-eb69-3f89-aeee-62b187257a04 | -11.3976 | -44.2167 | 2026-09-23 00:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 14405fe8-618e-3d33-b0c0-2ee3275ca5cc | -5.7754 | -45.1053 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 6dd800c8-9a5d-30d8-b09d-71f60b37fc8f | -4.0925 | -62.0874 | 2026-09-23 00:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 6fdbccca-935d-32d1-9738-52ab8e348150 | -10.6283 | -53.9885 | 2026-09-23 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 36a9d778-6634-32f0-9206-08cf9e2b1113 | -8.9108 | -62.391 | 2026-09-23 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ea4a69e4-a82b-387e-a6f2-ff136c3abf31 | -9.9436 | -48.4827 | 2026-09-23 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 8a4b61f4-8977-3a7e-912c-e62a638c598a | -6.6146 | -59.9272 | 2026-09-23 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7b964220-da15-363b-b321-83aefdd10884 | -9.9439 | -48.4608 | 2026-09-23 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 61651d70-c26f-3ba1-8130-58c7036d3fec | -3.4781 | -59.5588 | 2026-09-23 00:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3343a718-dbed-3626-9969-63064a965414 | -6.6331 | -59.9265 | 2026-09-23 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 3cfeb2ba-826f-39d2-97a1-2066a5e8534c | -5.7567 | -45.1067 | 2026-09-23 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| f1067a83-bb56-3ea9-8b60-aa3ca1f931fa | -3.6946 | -60.5835 | 2026-09-23 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README8.md)
