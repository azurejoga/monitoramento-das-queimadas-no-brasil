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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35358eac-43cf-3e5f-a824-d6399dd3f538 | -11.66707 | -46.77298 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d9c8cd4-f3f7-35d3-9669-d0e9728c161d | -3.48144 | -54.62209 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1f73ca3-2fe3-3aaf-b380-3204304cb89d | -9.30183 | -47.41684 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aed42573-746f-3e8f-8e2f-9714cb9797a3 | -5.0607 | -46.18475 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8013c1c-a1ca-3a93-a1a6-4413f60760a8 | -3.40604 | -59.59206 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48617ec0-6f2b-3bc5-b42e-36cedf555b4e | -5.24399 | -43.97831 | 2026-10-09 05:04:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 457257cf-3ca4-3d84-9867-33b142e623ce | -2.54925 | -58.0372 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bab019e-dd2f-369d-8962-e0e2e0b53645 | -6.38804 | -55.27026 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc00c880-173f-3a21-94d1-db90c5d119ce | -3.01523 | -54.0495 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2384669-406f-36f2-88e2-078be260c004 | -6.49086 | -55.9502 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b50158f0-21ef-3006-9171-daab8e9a1ad9 | -10.87033 | -45.5393 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f3bf055-e2ef-318e-9b05-a536a5a1d9a7 | -3.48846 | -59.38079 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f133bba-1804-341c-88d9-0b7db78d3e81 | -2.903 | -54.02468 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a364802a-a8fa-3896-bf34-6deaacae2cd9 | -6.94299 | -43.6655 | 2026-10-09 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd386c10-3025-31a5-88dc-f019c173e770 | -6.40159 | -55.27665 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f4f0941-2047-3ea3-b113-92094baa0657 | -9.29982 | -47.46077 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8d39468-6407-3f0f-9556-4157aded5b6b | -6.15294 | -51.70331 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a5da91-c3d2-3b1f-8655-8869732686a8 | -11.99837 | -43.46421 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c49a89d0-27ec-3ada-89f1-13f3a11d83e5 | -2.99794 | -54.13354 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf672ea6-a0ce-3a7f-a269-18002fbb770d | -7.68639 | -45.42966 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 63d9592a-5631-31f0-872a-ef5e9d2df79b | -3.53621 | -54.66776 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aebaa967-71fb-3c59-9755-d2d071f27281 | -7.53855 | -47.12748 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e11084e-347e-3e91-970a-1c27a98abaa7 | -4.1008 | -54.02261 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45dcd7b2-bab7-3d69-b4fd-ae8e09716005 | -3.01953 | -54.24445 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ec8b3ef-3abe-3657-85e5-766786a21faa | -3.59045 | -54.68335 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c859c296-7c1f-309b-ad6c-c28ffbb38ce2 | -6.01615 | -53.4819 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99696b12-94a1-39c2-837d-e75b68cb2a0d | -4.66283 | -49.2351 | 2026-10-09 05:04:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d41532a5-e657-3648-84f4-430ec0a9ef97 | -6.143 | -51.76643 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0370e032-cdcb-3777-b7bb-f00e4c4d078b | -3.90256 | -55.89315 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bdc83010-49c9-343e-9f15-b0a31227d83f | -3.10148 | -53.95763 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4306ac0-067c-3cff-bc24-670ce41b768f | -8.2263 | -46.40432 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6f035a9b-ca00-3573-8fb5-9803fa219348 | -3.50253 | -59.26719 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 488463f6-d3ab-3005-8676-f6b80d01d02b | -11.06517 | -44.08064 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9f4ff45-cbd3-342f-8140-4fc93ad2b060 | -6.01242 | -40.96376 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8fa6ca1f-29ed-3691-a6d3-69b9a7c6fa5e | -3.31184 | -53.70889 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 680d2d82-6650-3d31-a828-a23ecbfd1e85 | -9.14102 | -45.81356 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad9934e4-ffe2-3e26-9b9c-a4ff99a719f5 | -3.95507 | -55.33235 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 146c80ec-ca2f-39f7-bea3-f4016fe56d68 | -4.82666 | -45.8347 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edf1fd55-c30f-3e15-9c35-7111e0885463 | -5.0921 | -46.21855 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f1c2f9a-c69d-3fc6-ba42-b29bd6b9251c | -2.9835 | -54.06502 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8ecf2f-80e6-3c97-a0db-17253cf547e7 | -3.55733 | -54.69597 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 284580a2-3b6e-386e-8246-8da5a775851d | -3.49265 | -50.48895 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb72bac-2201-3d01-b8f9-73f1f4c94368 | -5.7019 | -53.48278 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f01cb8fb-dcad-3c65-b9f5-2e0427f42699 | -3.74003 | -59.36851 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d03b472f-c211-357e-a3b3-5a3ccf0aa396 | -7.40231 | -44.76021 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c807283-da56-3f0d-b406-d5eabcb34184 | -9.79412 | -49.01626 | 2026-10-09 05:04:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e46cbaed-7d25-392a-854a-096b83413dea | -6.16633 | -53.31683 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52c7194d-4640-34d5-baa1-2b067ce138ee | -2.51405 | -56.3251 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a9dde60-fd18-3d09-86c3-4333219b5bf1 | -4.98307 | -46.04333 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcda7333-7c5f-30c1-b250-0923585521bb | -3.08347 | -54.25063 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ef09b57-0cd0-3f11-800b-12e99eb73b05 | -6.31614 | -54.80857 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0545dd81-d71d-396d-b550-77a92df7f6c0 | -6.39334 | -52.72644 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f96d0461-423c-3687-9012-20d5525e1958 | -3.08162 | -54.28544 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 488991e2-e991-3f68-8961-bf89308ca5c8 | -7.83059 | -44.569 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2985e6b-6eff-3cbd-bf5e-514daec5fbab | -11.2516 | -47.74252 | 2026-10-09 05:04:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01378fa5-f613-3bc2-9383-b6f65f503ca7 | -4.10954 | -54.62344 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f64b049-7997-317f-90ea-71f1cd607657 | -3.07838 | -53.94616 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b311bd6-8208-3d6f-a1aa-0eadee725be2 | -5.10447 | -46.2247 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6436c374-3e81-31c3-bbb6-d210b4266761 | -7.08104 | -52.67949 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdab46e9-bafa-3cad-aed6-c19dcdeb88f3 | -7.08271 | -52.69044 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cbd2858-09e6-3eb5-98d3-fc3b97045618 | -9.09077 | -61.13647 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8ed6ed1-6803-33ad-9d33-1fe434864ec1 | -3.08739 | -54.29437 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea358c5-7f03-3e98-94ee-836f81819d84 | -3.80835 | -49.94107 | 2026-10-09 05:04:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5be662a-5ff5-3fe3-819f-28afafa342e9 | -4.45465 | -50.22844 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64eeb9cb-8215-3e27-a5b0-4cea223767a0 | -5.99104 | -55.36275 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bc50666-75f7-38d6-880e-0d0b8b56f953 | -6.67107 | -63.03043 | 2026-10-09 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6399671-d584-3cc1-bae4-6f5a8da96b7c | -6.22823 | -52.89643 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 852c3ac0-c153-328e-b006-ebcf0b187300 | -6.88299 | -45.88685 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3312fae1-5a5c-396e-9479-b783e23e0aad | -5.85594 | -53.46309 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b5ebc1d-eb68-31ea-86fb-c58fecefa040 | -2.39211 | -57.89357 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 340a0e72-75ff-37bc-a4c4-b19109623afc | -6.49705 | -43.95227 | 2026-10-09 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 495c73ca-c1c4-31df-b8ae-3adb5373fb4d | -2.97774 | -54.05622 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85c5e488-7967-3dc7-bb39-cf8404736aae | -3.02096 | -54.05827 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24aa8d18-11c0-3a35-b72d-c9a79b642639 | -8.70667 | -62.42328 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f14acd8f-5771-3597-b7eb-ec2c78fb4604 | -6.3874 | -55.25875 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc46ae1-ec2f-305b-a781-1e3d578f0a68 | -3.4652 | -59.25816 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d8ec99f-12f7-398a-8c5a-1c21aa12d467 | -3.01207 | -54.75488 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 231fab6a-d745-3f60-bab6-66acd18be579 | -6.07503 | -59.8823 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b0550c6-0daf-3217-803a-bc4b84d4b45c | -3.00924 | -54.06426 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6795dcdd-2573-3525-8499-091448abd2ed | -3.27331 | -54.05761 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8da4150a-74d2-33a1-9713-b2a13aa43e92 | -3.24915 | -54.03038 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d0cde7af-aacc-3b16-a6e6-8568f0adc7f8 | -6.38105 | -56.23071 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b66551a5-6ae4-397b-9e9d-918f1fa0ee7b | -5.10941 | -46.22117 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0e86d16-b8e5-3c68-9fc5-dc4655a14d72 | -5.85028 | -53.47681 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ef89663-b19a-3a7a-86c6-474eabba33fa | -3.65307 | -54.52166 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631dc7ca-6005-32cc-871e-798d66a07b76 | -8.96953 | -45.15549 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f19f5e29-4172-316e-9d53-2c587268b0f1 | -3.47805 | -54.73284 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd80a0f6-78ce-3fdc-864e-85cfa9a69c1e | -10.42568 | -47.28591 | 2026-10-09 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6bd454b2-d247-3bbf-a27d-b2a940bd48fe | -6.12705 | -53.05922 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d942a4d-0ed8-31a9-89e3-39a38ad8e45c | -3.16213 | -54.72303 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd490732-9c38-34ca-b136-04045ceb462e | -3.00546 | -54.2422 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6de476a8-9ad8-3064-82e6-e2c87e495974 | -11.11489 | -45.68426 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47dd135d-607f-3a07-893b-6a3b10f20806 | -6.95915 | -45.27832 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7c43cfd-e41b-3e1d-a917-65e59fe8897a | -8.91459 | -45.22669 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 276703a3-5642-35d4-91b3-b9e57bc3e8e5 | -9.28568 | -47.43874 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b8306f7-9c62-3566-a9da-bd8b3cb1d9cb | -6.4834 | -55.29008 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de7f1fa9-0218-3761-81b1-84c7db69f97a | -3.08833 | -54.26652 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a312a510-e070-3a24-99bc-4009f9e8c868 | -3.20229 | -53.8722 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84f47205-5e53-3251-a775-e0897a7da154 | -3.31785 | -61.27133 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98eb89b2-d8e7-3f10-a247-6db3f3434e25 | -2.98062 | -54.06062 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README149.md)
