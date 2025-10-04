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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eefc64d2-642a-3653-8f53-6d153f7bfadb | -11.15341 | -43.40032 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87616915-99f4-3b29-9275-f91c60ecfb52 | -5.72796 | -44.5084 | 2025-10-04 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65f9c384-dace-3935-8ea1-e4a9af18fff5 | -6.6993 | -42.6792 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3c363a60-744a-3da5-b6a5-65813b9e56d7 | -6.60973 | -44.29778 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3364c1fb-577e-36d9-a5d0-7468c68a142a | -11.49684 | -45.01471 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f85acc6c-f3d5-36db-bbc1-9a92ff863b51 | -6.60321 | -44.30722 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe935d14-90f8-3b19-ad73-a91f1b68956b | -7.71358 | -42.58202 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45736296-7f68-3406-be90-8594e87eb183 | -7.71683 | -42.56324 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2bee21ad-ada1-3bf3-b9ef-a84bca5b873a | -9.90835 | -43.73285 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9437e810-735b-35f8-a1d4-40621b66f144 | -7.72958 | -42.58864 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6aa27215-ecf2-3529-a597-a654aaf56e6f | -4.82067 | -42.76343 | 2025-10-04 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1e031033-9927-3142-b82f-1b862cae243b | -6.71246 | -42.79905 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 66cd8cd4-67b3-3767-8a6d-dd9fc13d3674 | -6.64441 | -41.95506 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e915f04f-47e9-3490-8eec-a0f2622cecd7 | -7.48098 | -43.03576 | 2025-10-04 03:51:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 726e4ff9-6737-3bb3-b927-c0610eeaa99d | -10.32478 | -50.35377 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c5a60c3c-2db0-3592-8329-1d7b5a38df6f | -6.17598 | -44.28706 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20bbd2af-4fe7-3d47-8104-314acb46b0be | -9.10916 | -44.39613 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e44ac5a9-e964-36f7-8368-8de158ef5a4e | -6.67116 | -42.83336 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a49b0efe-e1fd-3fcf-8d2d-a542c0cc5d74 | -7.8586 | -48.20087 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bcff18f-f358-35fe-a1d7-3bb7be5971be | -7.47667 | -43.03505 | 2025-10-04 03:51:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 076e960b-1092-3423-abed-133951ac9fbe | -7.86219 | -48.20814 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 94cd3f15-0623-39d5-9f8a-58b99ba9a69a | -6.99988 | -42.30775 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77b3a2ca-9c89-3a88-837f-9fe31f6113fc | -7.73702 | -42.95386 | 2025-10-04 03:51:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d256bfed-6a4b-3533-8eb1-f4b9a7ff593f | -11.05126 | -47.78766 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ebb9528-3546-3ca1-b342-a9497603e14f | -6.3737 | -43.90093 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 217cbafc-5e27-363c-b9ed-d169bc081658 | -6.19889 | -39.6988 | 2025-10-04 03:51:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66a29d47-4bb5-3492-9035-fed585a53cce | -9.94512 | -43.75241 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99bc6a5a-16b2-3ea8-8781-a6430f0b479d | -6.696 | -41.9461 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4a44dd01-51fd-3bbc-ae60-4444604a247c | -5.93702 | -42.88616 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 573ddd0d-dbdf-3893-a1e0-21ebf2a0ff48 | -4.44059 | -43.24561 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e3a58bdd-b2b8-368e-adb0-bb67c8210ab0 | -6.46277 | -44.58707 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 74598dd7-1e3e-3c52-9e11-70c4754985bf | -9.90871 | -43.80677 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 339cad06-014c-3bcc-9329-05732864bb10 | -8.22858 | -46.80953 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a223deab-4427-3e55-af6b-556eaecc5d00 | -7.34473 | -39.17363 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a1df0067-1ac3-3dc8-a0de-8be63eac8b5c | -4.27698 | -48.87886 | 2025-10-04 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 525ae595-357c-3733-8667-da46834eaedf | -10.99997 | -46.68227 | 2025-10-04 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d7257b8-0dfc-3c13-97ca-69e4cf2eeb4b | -6.34809 | -43.41085 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d82b61c7-d228-358c-b73c-30d176529558 | -7.70307 | -42.56857 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7435729a-ad21-3bf4-893b-66590b7b14c8 | -5.65758 | -42.73153 | 2025-10-04 03:51:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2213809e-e4b3-3bf0-b222-73972c8226ba | -6.17292 | -43.92863 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b03be2e-c79d-3e69-aa57-94c88b0c3634 | -7.77076 | -46.27406 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09218fd6-293b-345d-9c2b-68ec5aba116b | -6.34964 | -43.45695 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a7ac740-9c3a-334c-a843-0f95c2b0390a | -6.13512 | -43.81183 | 2025-10-04 03:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef797c61-da4d-3fd8-9f49-d89baa04de0c | -5.93587 | -43.30819 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69ded8ce-5574-30d3-bf67-78c433f54639 | -7.79161 | -42.57605 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4cdd9976-42fb-3c60-8fc7-becf4133a163 | -6.2463 | -44.24837 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04197a2b-dff0-3aea-97db-845bf7f32c83 | -5.20296 | -45.07178 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a11be47b-18eb-35dd-bc11-456306dd7480 | -7.72276 | -42.60337 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7475c47-e552-3fec-802c-24d9621fa936 | -8.22306 | -46.80875 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00995888-7744-38ca-889a-04003b720843 | -6.72131 | -42.16298 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c748be0-1d95-3ab5-b2f4-c97d7e9ad28c | -7.74189 | -46.31223 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a390b3af-a5db-3743-a550-eb5e4ff448d8 | -8.90763 | -46.60336 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a7c5993-c631-3426-831f-347d4dda6dcd | -5.71905 | -44.23842 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2782623-d0f2-3ff7-b016-eddfb10e7ce7 | -11.11248 | -47.87817 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab020f7e-dc6c-30c0-93f8-d9be6daaf806 | -8.53884 | -47.21558 | 2025-10-04 03:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e12614ad-1319-3e4a-8897-3cbd40a905f2 | -11.4441 | -43.49466 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e09c3fb1-fec7-3954-bbe1-b5add271a59f | -11.15132 | -43.38803 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 04778d27-2c29-308a-a664-bf953f59534a | -7.33094 | -41.44606 | 2025-10-04 03:51:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae7fed94-410d-3bf2-a5f3-dde5c5937de3 | -7.05562 | -42.78897 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 19ddba77-7939-3562-806b-49ac42aa65c6 | -6.07874 | -42.51081 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| a6797a63-b2ba-3cd0-9eb0-eedb8396037c | -6.30848 | -46.33347 | 2025-10-04 03:51:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7a65b44-7868-33e0-9d6c-82d3f4f69ab1 | -5.97578 | -42.94984 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 71d12dde-5bb4-3110-98aa-dec6810a3376 | -7.7346 | -42.60938 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75c09471-2cba-3c29-84b5-1658db726eb9 | -7.71292 | -42.58587 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48b5e032-f120-3e06-8f30-9a4556527e78 | -11.50039 | -44.99552 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b73aa027-9c89-39ab-b3f4-06e450190ed9 | -11.51135 | -45.01324 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cb67bdd-02f6-3f1f-9332-78e76aa87038 | -6.68264 | -42.84381 | 2025-10-04 03:51:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5241b68c-fd80-31ea-95d7-9f338940504e | -7.77539 | -46.24808 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 728ccc87-355b-35fb-bdfc-2cc4921598ce | -10.74029 | -44.70586 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6375f639-16f1-30f6-9f13-c6d641370277 | -10.93422 | -48.83217 | 2025-10-04 03:51:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bca499e3-433c-3aec-b406-a6ecdb2a8956 | -8.71085 | -47.98802 | 2025-10-04 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| caeeb97d-a67f-360b-a92d-104cb74a4134 | -9.94944 | -43.75325 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74c57a4d-0bfc-35f0-82c7-070cfcb9412e | -10.33945 | -50.31549 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc2c4942-9640-31f7-b1eb-d84154194209 | -4.66689 | -45.80577 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c23a621-38cf-3063-8366-587d4a99a46b | -7.75389 | -42.54647 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c0e00552-5cdd-3f35-aded-b01de55fc7f2 | -9.75625 | -43.62223 | 2025-10-04 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40f49e72-4e04-3aa8-a3dd-b535e48042a9 | -6.36909 | -43.8999 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0be0d778-1390-3aed-b33c-fa5d1d4a0592 | -5.93387 | -43.30994 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecb9273e-5b73-3afb-b168-6666b4d78f65 | -4.66748 | -45.80229 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5c882f1-fd26-3c82-a595-b0a1d4de628f | -8.84004 | -46.83903 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b00ace1-0774-3536-840a-9f4ada043810 | -7.54457 | -42.40691 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 41c86e75-33c3-3c5c-8212-7bf75640e82a | -9.95234 | -43.73662 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7200df0d-9d69-3089-8ad7-657d3338fa82 | -11.10798 | -47.75177 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 19bddfa4-e562-319d-a1f6-3aedb5167389 | -8.84854 | -46.82319 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08d1c370-f74b-3243-bf8a-af232ca2a0c8 | -7.86291 | -48.21098 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49953d4a-f256-35ab-8794-a6a0f33a9e6f | -6.65306 | -41.9533 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58268c07-9070-3056-9161-0fcbef391064 | -7.7405 | -42.52491 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dba32bb7-8304-386e-b839-0aafadd20ce9 | -10.06892 | -48.18383 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a82e0024-1c47-33cb-819d-ddeaddd544c2 | -9.67948 | -37.09132 | 2025-10-04 03:51:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d0f5b3b0-b6f5-3925-b388-c643e72faf59 | -11.49221 | -44.98849 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1d8ffbc-0258-3b4f-bce5-2834b3bc4a0e | -8.8495 | -46.78731 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac2d814d-eae3-305e-a782-bf28c334de71 | -10.01642 | -48.27497 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c48776ac-e539-3286-8990-f0d2e5f2f87c | -7.77757 | -42.60877 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c94566d2-bf70-329a-ae9b-992b00978d80 | -7.71618 | -42.56699 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d8cb973-d575-3750-ba74-c647613da743 | -6.06621 | -42.51358 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6cb97808-dc18-3d84-b459-aae3a7e0b204 | -7.51473 | -47.56536 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61bfb25d-fcd4-3000-8b45-d8f404e52341 | -9.90701 | -43.71521 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 215cf85d-f149-3d05-833a-ec3321687123 | -6.67121 | -42.8217 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6c6d4b24-6e05-3619-8764-201798260129 | -10.84537 | -47.20568 | 2025-10-04 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6af7fdbb-e907-3d9a-9003-cbf4d21caeda | -11.08131 | -47.88957 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README26.md)
