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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d20525ae-68db-3207-bec7-c055b1a93aca | -11.67368 | -44.29362 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6901468f-de51-30d3-ae12-64a29e5b118e | -5.40838 | -37.70123 | 2025-09-30 03:47:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9e216ba5-c0f4-3bf8-8649-3e4faa2bde41 | -4.89964 | -43.47559 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08848bb4-0da6-38f5-b801-fe6463972b09 | -10.1076 | -47.78074 | 2025-09-30 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a767e88-e78c-3f65-8397-21193c9fda6a | -11.43562 | -43.50648 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fdae6d4-2f11-3abb-9f25-49c2a86dcf9f | -4.47796 | -47.67226 | 2025-09-30 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 106a5a55-2a35-3e8f-b58d-bb9f10a49b2b | -4.81871 | -42.76493 | 2025-09-30 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68c4dac2-5a5e-3566-bff4-ef465e9b2a22 | -11.4933 | -43.52143 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8161f12-c567-3b89-915b-25d4423d1a54 | -10.95698 | -46.49924 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c966dca9-c6af-3c0b-ba70-506d930c7918 | -10.078 | -50.22171 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c9ad00d-8c0b-37d8-ba26-1593e998f7a0 | -8.87221 | -46.61179 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50412d94-a18f-3102-aec8-8f151d2edcc5 | -3.10452 | -47.01418 | 2025-09-30 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 76de867f-0816-337e-9c4e-63698107cdc7 | -5.42034 | -41.32547 | 2025-09-30 03:47:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7138183b-f20d-3ab5-bb2d-e4e0cdc4f6ac | -4.89498 | -43.47486 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b7416bff-dbf7-3ed7-b80a-9e20ef6a78d4 | -11.42867 | -44.94628 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cc771f6-ab11-367a-a2ce-7f43a907fa3e | -11.43325 | -44.94725 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db0a0363-2b96-394f-9147-344d38a55ad0 | -7.47826 | -47.2698 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b307faf-d5d1-3bd1-8395-0d30611b8eb4 | -10.20126 | -44.89501 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9de7bde-4de9-3ad8-8536-2c8f99a0f587 | -10.39688 | -48.14468 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 643c25df-8a2b-3cd1-aafd-5103140bb6d7 | -4.86479 | -45.05134 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f42c2f5-8c5f-353b-b779-1f4c963f6e29 | -5.25064 | -42.90013 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0027e99-7498-3ca0-b514-859752154996 | -4.14573 | -44.42656 | 2025-09-30 03:47:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0396b3ad-ef6e-3280-b50e-1758e6283fc9 | -9.8865 | -45.96049 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521803af-e370-38a8-bf39-db53b1948923 | -5.5152 | -42.72469 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0fa77eda-dadc-3430-ae14-6ef9c4c260ed | -10.84612 | -47.96193 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9da48fc0-fb95-3744-abcb-888a698520e3 | -10.83974 | -47.96458 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c1a1e77-2be6-339c-aa05-181f7b9073c2 | -4.15564 | -40.01028 | 2025-09-30 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 60ebfab2-84b4-3c53-a237-e86a4216693d | -10.53247 | -43.64403 | 2025-09-30 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1323a34-5351-37ed-9753-5418c23e3ccf | -7.76041 | -45.76717 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 599e2922-bd6d-3abb-885a-05ed6fe858c3 | -10.53322 | -43.63987 | 2025-09-30 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36a66958-210d-3a17-b3f5-70e45f257594 | -10.06423 | -48.19261 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d14fb333-23b5-379f-888c-c9fc390fa1d8 | -5.03521 | -43.61321 | 2025-09-30 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a8dec798-3aa0-34cf-941c-e52fd1151a9b | -7.84426 | -47.26314 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8173abc-0ba7-3046-a237-b9ca15a06ac3 | -4.90045 | -43.4707 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| f0ea2e08-13b5-308c-a480-91ea0389c92f | -10.18382 | -44.89923 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9812738e-d019-3b64-884c-e9f1c95fd0fc | -10.83392 | -47.96428 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6467b0c-81b8-331f-8ca5-857d7382bc0d | -8.53727 | -44.6385 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8b288b9-982d-3ee7-984e-1059ac56e6f6 | -9.20007 | -45.93686 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c612ee4-cd10-376b-b6e9-46bdfa861496 | -9.30002 | -47.37697 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67e84dc7-a2a5-30ba-beb5-ee6dc7ce9a62 | -11.67651 | -44.30311 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9de0d17f-daac-33ef-9989-882b8020b2ff | -10.83997 | -45.41392 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a9fac88b-558b-31b3-b9fe-0daebb097834 | -10.76906 | -45.3721 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f70622f5-611c-3402-9401-6c4e0183b0a4 | -11.51104 | -43.54835 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b772c4-729c-3fc4-8dc9-5a8546742e1a | -8.22734 | -45.50756 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24073224-fe50-3d6e-8aaa-a345faeef9e2 | -9.88536 | -45.95815 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d4a3022-3d27-37d4-bb53-11fa6a3c3b03 | -11.45808 | -45.0205 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e022344-fa8c-3145-9112-72187a5c4c47 | -5.28028 | -43.16304 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8522c540-6046-31ec-ba54-fdc79a6f08ab | -10.03616 | -50.20118 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc2598e0-b8a7-3552-9918-f95a464077b1 | -7.75929 | -45.7736 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96963ead-1093-3586-a593-7325993b04ef | -8.53574 | -44.67451 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f22d33a1-67be-320a-a656-bad70f04609d | -11.37172 | -45.07449 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa7e15ce-4aa6-3a1c-a033-f6e9a9220d3f | -8.96332 | -47.45146 | 2025-09-30 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d64bfe6b-33c9-3e49-aebc-c64e15fa54cf | -7.82721 | -46.99019 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e28f08e-6f99-3036-8b81-e19fa77e0edc | -10.80634 | -45.35758 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df6fa3b9-9c7b-3b45-bf2f-10a9ad327920 | -10.18544 | -44.90214 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| e38f9660-9ebb-3dac-b7d4-f2d52818f506 | -10.39158 | -48.14115 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81d080fd-13d5-388f-a790-8a4737483b3e | -4.0058 | -43.27628 | 2025-09-30 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50d519dd-ef49-377e-b7d7-9b40a52a6013 | -9.93685 | -47.46286 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a02aca6c-9bed-335e-a349-ac06d6c87268 | -8.88885 | -45.03839 | 2025-09-30 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eb419ac-a1e9-3540-9e55-7b82d8a26bca | -4.34986 | -45.58466 | 2025-09-30 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc9f1190-1f4f-358f-9d6d-dc3a30047ec4 | -10.63759 | -48.5742 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c423e59d-18e9-342d-bdd5-950afabc2186 | -7.90956 | -44.62483 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e7bb0602-693d-3601-a2fa-e33bc245765b | -9.32346 | -50.63633 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d80370f-d01e-37f8-a31e-0e25feba3029 | -4.66305 | -46.46611 | 2025-09-30 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60ad7927-0d87-32b7-b44b-f21ed00da8ad | -10.18636 | -44.89715 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 90861068-7016-3648-84ab-a853bc05c6a6 | -4.47715 | -47.6769 | 2025-09-30 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06b008f6-f89a-30ab-88e8-0b71f4939f91 | -9.37492 | -47.58844 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920b577e-dc97-3950-8556-2ef3fd5787e4 | -9.12154 | -47.63444 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c63c0b81-0015-36d6-b782-76fa4ec36e6e | -5.04385 | -42.896 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b68bb100-db19-3858-9a71-8ca2116b586f | -8.2478 | -45.53081 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e21dc35b-3a7e-3aa3-a71a-b15f051ff58f | -8.64874 | -43.98491 | 2025-09-30 03:47:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f635289b-eb33-3f6b-aa4b-da8e6ff26daa | -5.02805 | -42.98938 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8e6905c-54b4-3b8b-9298-7906872803b9 | -11.45871 | -44.99047 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 893679af-e260-344c-9621-135c6496180e | -7.76986 | -45.75056 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fe96ea9-e55d-360b-b7d7-2ea8b2e17c60 | -10.18559 | -44.88923 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| aa8c53a9-2059-3241-a31a-6b2a8b202af8 | -4.396 | -44.07538 | 2025-09-30 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 56b7f47e-267c-3c0b-bb24-6859285beaed | -8.49844 | -47.25444 | 2025-09-30 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6408312-f639-3faa-a2ed-3201e20d0041 | -4.39747 | -44.39669 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68a4384f-6f23-3a46-9cc8-15c3c1b07dc6 | -7.76646 | -45.73991 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc4a721d-b05f-3418-bffc-e823d42732c3 | -9.12799 | -47.6382 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64d86718-d7b0-33f0-beba-73f140376749 | -10.39204 | -48.16991 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7bf91c7c-d162-3363-8abc-a7c6d437e37c | -4.97776 | -45.30141 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e122b0a-453d-337e-af5e-c0bb4ec36a3c | -5.37239 | -42.84868 | 2025-09-30 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 046a1ccb-563e-384c-a306-2f2d897e72be | -8.87376 | -46.63385 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9bbf4a43-c40f-33f0-9bd2-37fce5c4b1ec | -2.86414 | -40.47174 | 2025-09-30 03:47:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dabe4fce-b448-3658-8967-7785a9d1cf8d | -8.67122 | -47.70789 | 2025-09-30 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69c846c9-2bc6-3995-9ada-f249d38606f3 | -2.92732 | -39.98282 | 2025-09-30 03:47:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11e23e27-4cd7-303d-bbd2-85fa2663d0ec | -9.32512 | -45.69991 | 2025-09-30 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 264ea6d2-a55e-320a-8782-5949f696d76d | -3.80768 | -47.57698 | 2025-09-30 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9787724-0423-3741-838b-d818f83650d9 | -8.25652 | -45.51156 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c9bd80d-e5fe-3b4e-be72-74aead37fdc3 | -11.51081 | -43.5446 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46f87215-bdbd-3cb7-a01a-a74a5a42255a | -11.4407 | -44.95855 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b1afbf4-af4f-3a19-af1f-09862b9cf13a | -9.37148 | -47.58636 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dac4082-c8a5-3f82-bbd5-694c5c9192f0 | -10.39923 | -49.04966 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a610db5-f439-331c-ac76-09a6e29577ab | -11.45837 | -45.01316 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77651b72-10db-37aa-a639-73d4f7e02b89 | -9.05858 | -46.71261 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b89a98-53d6-361b-a1d5-222b562bae0e | -2.806 | -41.80044 | 2025-09-30 03:47:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f57b16a-c7db-3e31-a788-a494864a0b2b | -8.66821 | -47.72421 | 2025-09-30 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5104e78f-a5b9-3753-87c6-64a31573f18b | -9.1995 | -45.94 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c2a4db3-1d09-3faa-bd7a-b92d5551af21 | -10.08457 | -50.22308 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |


[Clique aqui para ver as próximas entradas](README24.md)
