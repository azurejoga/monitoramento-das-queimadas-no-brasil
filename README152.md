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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa651e16-8819-3c17-8950-737ad99fa937 | -3.09331 | -53.96414 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd845e9d-78df-3b40-ab2a-4c811251cd05 | -6.44319 | -55.04716 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2d13079-2ec9-3e74-b3b1-a32498860024 | -2.87788 | -54.18312 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5250d083-4c4a-31ba-9eb5-cb0e4b491880 | -3.21024 | -53.88896 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8c0225f-9e04-30af-8f86-19f8db300e68 | -5.14297 | -48.86856 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fee8b58f-1ffb-3a77-a67b-29efb54a1b9f | -4.51949 | -54.98418 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea39d8f8-66ba-3731-ada2-7fa007ae03fb | -9.28256 | -47.4303 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 73e77b9a-915e-3651-af6d-db55cf524141 | -11.31144 | -44.82774 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 631ee082-089f-31cd-ab00-23c32ec4c31b | -8.90969 | -45.22594 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf0e8905-470a-3ddd-a766-282cd5cb3c81 | -3.09697 | -53.9413 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80776198-3bdb-3914-86c0-55d5a3a523ff | -3.57554 | -54.68502 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebb037ef-004e-343e-aac6-83e04a3392e2 | -6.49503 | -62.85497 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eca94c3d-feb7-3ecc-b31e-67236ba218d7 | -9.89913 | -44.79271 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d89162e7-831d-3299-8a3f-7a87d7beb6c5 | -6.15578 | -53.30825 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 557c2e66-952e-3a39-8abd-13683b4b8a63 | -7.39812 | -44.75405 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 22e71f4e-8e20-32af-ad24-7da9f46cce02 | -5.2385 | -43.98057 | 2026-10-09 05:04:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18d737cc-66a6-3e5a-84fc-0312addc36a4 | -3.01249 | -54.24333 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d932dea-42a6-3676-b284-b97cadea81ed | -3.71599 | -59.65142 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fffaae3-4fe2-31c7-9cf2-cc8ce8a46b37 | -3.72355 | -54.21699 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f81f5463-bcd8-3600-a425-f91b3004764a | -2.97838 | -54.11958 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4edd635d-0df8-3388-927d-dbf7ccfb66c4 | -8.32415 | -49.12298 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bce90222-6e10-39a0-a764-fd599fe3f8b6 | -6.05082 | -52.75049 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90108d6c-2397-3c5f-9590-7ee9916f24b5 | -6.14355 | -51.76293 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec84cfda-7de2-39d7-babb-2742b0f889bc | -11.05686 | -44.05779 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71b67c01-ab49-354c-8ba4-c4b6171d516f | -6.49357 | -55.30764 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98f9e3f8-08c2-3705-90d0-16802827b7a4 | -6.45595 | -55.48907 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7aeb84-8e2a-3f60-8ee0-30339e20c25b | -4.1089 | -54.6274 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8f2eb3e4-7eef-3645-8092-a86e062747a4 | -3.13718 | -54.36682 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5df0f8a6-7e82-3b2d-9505-b97d326eb150 | -3.27781 | -54.07405 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe6452d7-6b86-368c-be6c-4bc66ed6c5b6 | -5.09155 | -46.21505 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f92282cb-6887-39a6-a2c0-fac6091f55a1 | -8.00257 | -47.18842 | 2026-10-09 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b1b4ecc-b377-3b8c-ac9f-31adfe18790d | -2.89288 | -54.91132 | 2026-10-09 05:04:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0965c7e4-5968-3d24-bb98-c4c3d1cb9809 | -10.87388 | -44.7981 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e4c5200b-28ec-3a5a-a3c9-cab3865d4ef4 | -3.27904 | -54.06638 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6cd61d4-1850-3b36-a4b7-05cbb6515305 | -3.57422 | -54.69307 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5e556b3d-4ca0-3bcd-9ad8-4de5934c0ab3 | -5.07362 | -48.40754 | 2026-10-09 05:04:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ae7f72a-60c4-3a15-b1b3-9e35cd80f082 | -3.25836 | -54.03963 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8802ab4-d096-3cee-8513-ddf8e1148af4 | -10.88513 | -44.7929 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92e0e0a9-3559-3c24-a71e-02281f79a150 | -9.69057 | -58.09082 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dead7f1-8b39-37d9-9e3e-0abd3e396e9f | -8.22059 | -46.41238 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aabf3e1f-e51c-35be-a0d1-9201bc2d47d8 | -10.98969 | -45.40176 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9f215d9-ca38-3301-aeac-f2c564aecc86 | -3.72006 | -54.21642 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 274b9236-bc88-3949-ae6d-024d05de5d75 | -2.93534 | -53.92033 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 813e87be-f63e-3d6b-8a01-1222152c23fa | -4.69036 | -56.2257 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d9542f1-5afe-3884-9b61-1c6d2386ad9f | -11.27094 | -45.1853 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9df4096-af6b-3759-8395-3b516de00150 | -6.30693 | -54.79916 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f755d722-4154-3efd-af95-e20cba45949d | -3.27494 | -54.06966 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17f954fb-f698-3512-8bac-ee6b9581ed7d | -2.95137 | -54.19865 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb8a7069-e0e7-3049-9806-4e35cfed0e75 | -3.00113 | -54.0442 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a1fa660-09d8-308e-99dc-648cb66d6c93 | -3.00479 | -54.79302 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5050518-1c47-3773-ae6d-2d4fbc4808a8 | -11.6754 | -46.77214 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab36973d-f615-3f8a-8841-0161c29a81c0 | -6.59962 | -60.0471 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 023170f9-ab09-3a3c-bea5-029ea19413c7 | -5.23672 | -60.18635 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1ee363a-2ad1-35ab-b055-486194c1d89d | -11.46152 | -43.38691 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c68c75d0-7557-3bb1-8f09-6f534b91bf0d | -11.1989 | -45.31818 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 468aa363-792e-3f9b-b044-b6518aa27ff9 | -3.78822 | -59.37313 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d628bf6d-b230-33e3-bb0f-5c479474524f | -3.96886 | -51.8699 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2be518a-bf14-38c2-8097-a8c46b5a7c91 | -4.92009 | -55.85994 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ee926cb-2783-35e0-b1e3-cda1bb2cd455 | -3.26634 | -54.05653 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00250324-0c3c-3b81-a9f5-008b3d8f75b5 | -11.27564 | -45.189 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92008dde-92f7-38ec-9d7a-bc3622af019e | -6.23152 | -52.78993 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86e5d7a5-d830-3fb7-adb7-233f800a1230 | -6.49291 | -55.31165 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a74b1a0-7b60-3408-93a5-c45238fc1dde | -3.0317 | -54.14689 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a03b868-d398-3743-b17a-b23424ace60a | -5.6985 | -49.08456 | 2026-10-09 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d59306c0-3ef5-33c3-b826-5c2c61541c64 | -7.40726 | -44.76098 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4fad074-d090-37bc-8926-b648fac7af69 | -6.44932 | -59.9537 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c60125d5-c69e-3a74-a58d-b2fe1021d9ba | -2.58423 | -56.18491 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d80d9cae-2a1e-33d5-b1f1-afb7d6c92b66 | -9.86787 | -47.47567 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3228275-f50c-35a7-ba05-9249ba5fce31 | -3.27269 | -54.06142 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6f80d25-9313-33e5-aaa9-4999de576cc1 | -9.22567 | -60.87717 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4fa2d8d-3195-3f6d-8efb-cefee9eead4c | -4.12967 | -59.89543 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0a52349-9857-324d-b62f-5eef375808a7 | -6.49068 | -55.30305 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e8f05bf-15ea-39ee-8903-7830efa5d48a | -3.58398 | -54.67818 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1aabe38-ab34-39da-b391-d51635ba2d3d | -6.32089 | -54.80135 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8cbfc1e-40a1-39ea-8a6e-ebf5111f7dcd | -5.69857 | -53.46038 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1c6e8b-ae29-37e1-befc-aa96ceefa94f | -10.87949 | -44.79559 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a825656-c53c-375e-87b6-c8d828ca0500 | -4.30074 | -48.60406 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a44f15fd-cf29-34eb-a63d-aca519173380 | -5.10571 | -46.21622 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 985a3a88-3e29-37e4-8f46-dc7bc4e2ee43 | -3.9804 | -56.11111 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8113627a-2af8-37af-9b35-65d53d375df4 | -5.10075 | -46.21988 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2266b72-2b3b-33d0-b86d-cd8b4d00fbdb | -11.01539 | -45.43442 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 4482dd1d-8e26-3c77-adcd-3772359e004f | -3.5376 | -59.40694 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 493e3f7c-8f51-3e17-9c85-af56beb95b4d | -9.87298 | -50.4952 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f159af9c-36e2-34f6-b070-03a18d031865 | -3.52747 | -58.14626 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b692990-a0f4-3f0f-838e-281e1c40f3d9 | -2.98515 | -54.07711 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9d6fa16-e3bf-39e7-bd45-1166dd986345 | -4.0357 | -54.22985 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35861cc6-51d8-31ac-b818-ea921d7835b0 | -5.92806 | -51.82267 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe55753-2465-3c23-b2b6-332cc8c55de4 | -3.43156 | -56.94153 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0529d37-2290-35cc-810b-3ffb130db1e4 | -3.11088 | -54.1945 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1d6a6b97-e73c-3ac7-baa6-6d3ef337ccd7 | -7.19144 | -44.27675 | 2026-10-09 05:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bbf06a6-35ff-34c8-92c4-e01caa15a44e | -2.94113 | -54.10563 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6649ea5b-778a-3667-a3e6-5fa3b37ec61e | -5.71585 | -53.48823 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d3c33a8-e834-3e83-af52-fc0b41412aa4 | -2.99744 | -53.91072 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8a00ca4-522c-3fd6-bc23-757acb655f4b | -6.87974 | -45.90974 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 84f4e2f3-8fa8-322b-b6fa-c02bcb60046f | -7.40386 | -44.7492 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d76418a9-5565-32b5-bd69-245ca226f584 | -10.86437 | -45.53671 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 646e1906-7241-3e15-9852-6c9d2bb70461 | -10.85865 | -45.54177 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42275c3e-9eb8-399a-bc7f-c49940beb8d0 | -2.86568 | -54.16922 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f958d751-d5e2-39e1-904a-a6d70f6244a5 | -4.63405 | -50.95348 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab01c23c-174c-38a1-bf36-aad1813aca39 | -8.07589 | -45.64294 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README153.md)
