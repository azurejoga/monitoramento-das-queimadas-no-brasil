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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dd7374f-2e81-3cd3-8aaf-3fb6f9fd723a | -2.72663 | -47.38667 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 227848c7-e8c0-3b93-ad04-2ebe107cc095 | -2.98866 | -52.81869 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c129c18-9fe8-3783-b267-886193ef0e82 | -4.58776 | -45.99489 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70bd6a34-25a5-334e-a641-31742f7471ac | -4.67177 | -46.30317 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e639610f-bba9-3e8c-bd01-e049aafdc71a | -2.98475 | -52.82168 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f86c67f5-78c3-3bd3-be29-4792b000fb0e | 2.55849 | -50.9809 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aba4d509-44a1-3f4c-9baf-f3cf1451f4f7 | -4.37564 | -49.63406 | 2025-11-07 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cacb4c1a-d99f-3e72-81b8-5aef187cc337 | -3.59095 | -49.44103 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aec17586-bcee-3fbc-96c2-feca7a95203c | 2.55681 | -50.99178 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbc0b59b-d834-3583-8aee-fc39bc5ca08b | 2.45417 | -51.00468 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7374b5f9-27b8-3a08-a053-43fa3ab76cdf | -3.76848 | -44.00772 | 2025-11-07 04:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 34957f04-fb0e-3cc6-812c-2eb5cffed45f | -3.05254 | -48.71839 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b0ad943-2ad3-320c-95c4-3cfada9a9ea4 | -3.38135 | -44.17186 | 2025-11-07 04:53:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58e84d3a-37a4-3f66-831d-9f26880df7e2 | -3.03868 | -50.30782 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e19c8b6b-4c2b-3b98-9d4e-52c1c663c306 | -2.32321 | -45.64664 | 2025-11-07 04:53:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90af0342-dac3-3452-bf84-b374b7e634ff | 3.641 | -51.8228 | 2025-11-07 04:53:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 637c7c22-cb17-3e58-ae7d-eb2be8d9e059 | -5.2663 | -47.16327 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb446917-02e1-3cbd-aa76-9563abe05009 | -4.45285 | -46.44342 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c128719-2bc6-334c-9172-97d49fa2210b | -2.85781 | -49.88235 | 2025-11-07 04:53:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51a2be58-d5e3-3c5d-a814-f1c3c092ac42 | -4.29967 | -45.88671 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 030d0595-d89b-31c0-a827-d97729aa6a25 | -2.94116 | -49.35387 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b98529c7-73c1-3afb-835e-a847794b616d | -5.75151 | -40.79717 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4de2460-b01a-3f76-a27a-39a41c0bda2f | -5.11816 | -45.88736 | 2025-11-07 04:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b953efe-a315-3aec-a3f3-560c1175ed7a | -4.68139 | -45.84447 | 2025-11-07 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bee658d3-30ef-3619-9068-135676db74c2 | -3.35056 | -53.22283 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cc88dab2-d1a6-3153-9b8f-2aec2ec25d6b | -3.45531 | -48.83578 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5565e1d-a44f-30f8-9e79-bf86ddf073be | -4.24985 | -45.62242 | 2025-11-07 04:53:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0c015bbd-fa04-3832-b3fc-b12720936466 | -4.01585 | -46.28435 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4589498d-f5dd-3728-a294-85431597d93e | 2.56508 | -51.0011 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 004ffe9b-c6c9-3321-a8b4-bfe7b6d16df2 | -4.44979 | -46.43489 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72bbe62c-7ce0-3fc9-a673-957be352fc43 | -3.37564 | -44.17651 | 2025-11-07 04:53:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7235116-46bb-3c69-8f37-75c5d9bbbe34 | -4.20432 | -49.73999 | 2025-11-07 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad5f292a-8cd9-3ac7-a406-0e45d5ce77ee | -4.31419 | -48.07756 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0418893b-4903-34ad-a72c-128008069dc9 | -3.54041 | -49.44127 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9c3470f-ed0c-3f52-829f-df962a3b439f | -3.59432 | -49.44041 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0e1eef69-a224-32a2-b957-8866ef1278d3 | -3.70173 | -49.56392 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e827a4c-ba56-3316-b4bc-84dd4848f09c | -4.29903 | -45.891 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a5623f2-5821-3d3d-969e-e181051b29c9 | -3.83782 | -49.90968 | 2025-11-07 04:53:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 707df8af-3891-3efb-9e42-b0ceb9695d9a | -5.58065 | -46.30605 | 2025-11-07 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48174cfa-021e-3046-81bb-23ef64b8680f | -5.63869 | -46.39588 | 2025-11-07 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c9d1b7c-26b2-3552-9e3e-58f327a0231b | -2.55204 | -48.39154 | 2025-11-07 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5f15bf6-e83c-30a6-97d3-12e572bd38cc | -4.68239 | -45.84673 | 2025-11-07 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fad88c5-5608-3f50-981b-5c64d5edc5e9 | -5.27397 | -47.16808 | 2025-11-07 04:53:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 885e0a9b-93f8-3ea6-9c0c-5be108a7f03d | -2.77945 | -50.29066 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9de80fd-bf3a-3843-9766-28545dad23a0 | -2.62766 | -50.07764 | 2025-11-07 04:53:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39b78c80-8b1a-3d56-8b19-eaae10a11ebe | -4.59282 | -45.99105 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2d4b838-5935-3710-aec2-84e2f7f7414e | -3.12335 | -50.14545 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02263b6e-acd2-39e6-bc7e-0e9c16faed38 | -3.34169 | -50.1781 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9239006d-3f13-34f7-81e7-8a8f5c3f340b | -4.44922 | -46.43868 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a3a0278-9611-3b62-8121-e5655fc05457 | -3.5291 | -47.54438 | 2025-11-07 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ae01db28-a379-3283-9417-e40ac3b11b32 | -4.11128 | -48.0177 | 2025-11-07 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6c7dcd76-00df-3454-a13d-9683f5ebd7c8 | -3.34511 | -50.17862 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 707adb78-5326-3342-a245-90f01a0abd2c | -3.254 | -53.27723 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ff3c4c9-0b4c-320e-8537-4f13a9a21ecc | -3.91611 | -44.41289 | 2025-11-07 04:53:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd02a6dd-60d4-3f35-bf74-81486f3f7aa4 | 2.55403 | -50.99575 | 2025-11-07 04:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 057a8570-5a0a-34a9-8e33-c48756a00970 | -4.61099 | -49.48634 | 2025-11-07 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44c9047f-241e-3702-8caa-8bd5ff827205 | -3.59492 | -49.43649 | 2025-11-07 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d5523e98-f9d1-31c6-a2c6-cf39dd4891d8 | -5.36822 | -44.73658 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3bce266-a410-3d29-b161-409dfa6886c9 | -4.57785 | -46.2984 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 348a9bfc-7824-3747-9f7b-37459d8eae70 | -2.87853 | -52.61432 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7a16b59-c292-372b-be49-b0bc72d98ec6 | -3.67073 | -49.83431 | 2025-11-07 04:53:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e00b175b-ce2f-3518-b964-baf231354542 | -2.89736 | -48.06337 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6c751ae-b806-30c5-911f-27996bf1e6b1 | -5.39797 | -43.93491 | 2025-11-07 04:53:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c109381-8d11-3f4f-923f-0dfe9db7d315 | -5.76408 | -40.79969 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ae6d6734-340a-35c8-9696-de173b9df6aa | -3.34719 | -53.22229 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3bb895f8-869f-3c56-97d9-6e82da812829 | -2.85437 | -49.88182 | 2025-11-07 04:53:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edeed0ed-1a01-3699-9b7e-fec17c1a1462 | -4.49491 | -45.13705 | 2025-11-07 04:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 56f6474c-81d8-3eee-8b5a-984c00f570a9 | -3.35113 | -53.21926 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9863de24-f5f2-3960-b062-fd3323cf414c | -5.08487 | -44.80397 | 2025-11-07 04:53:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4decc805-bd20-3638-81a4-f9a5c181a1e2 | -3.1474 | -49.21108 | 2025-11-07 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4574221e-7e0f-358f-94bd-a734635d1649 | -3.17327 | -48.61231 | 2025-11-07 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be9c59a0-32b3-3ce7-9ecf-7ce37e082e3b | -3.77862 | -50.03903 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1c96f4-65b2-34bb-b4fc-b5c6e55bd4ff | 1.3564 | -50.71828 | 2025-11-07 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e82c00-009d-3c07-93cd-9085cbbf5c02 | -3.77517 | -50.03849 | 2025-11-07 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b11958e8-170c-3000-90cc-694c1c8a0bfe | -4.04853 | -49.02452 | 2025-11-07 04:53:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 086c0869-bab5-312e-9b38-4b7b58e7e5c6 | -5.44274 | -46.35679 | 2025-11-07 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cc55867-70bc-38aa-a1a5-f80fe960456c | -4.31492 | -48.07281 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171076cd-f900-3cde-a96f-94ebb58d205a | -5.75778 | -40.79853 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 441917ce-fd37-3797-9db0-794c1d00f321 | -4.06713 | -54.84597 | 2025-11-07 04:53:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f004f2f2-4d37-3948-99bb-7cb1c6fd4da9 | -4.44439 | -46.44188 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5418f13a-dba8-3a67-8ba2-0d2e47ffe327 | -4.40127 | -46.43949 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3f38659-3e81-3b24-83e1-0bd5a28124e6 | -3.12051 | -50.14125 | 2025-11-07 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 12ad99c3-12cb-32d6-8415-980a83414ae4 | -3.34662 | -53.22586 | 2025-11-07 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ddc7711-1017-37f3-ac07-36526a088232 | -3.42511 | -45.23895 | 2025-11-07 04:53:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6629bff7-a8e1-3fcc-9461-032f111ab323 | -4.71249 | -46.42653 | 2025-11-07 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18740882-8a35-3919-973b-dff085426861 | 1.35363 | -50.72224 | 2025-11-07 04:53:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 791946dc-59f0-368d-89cc-d6d33dc1f160 | -2.722 | -47.39091 | 2025-11-07 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7d0c3ca-4289-33d8-9851-9ad388903cc3 | -3.76904 | -44.00283 | 2025-11-07 04:53:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 646e535b-29ad-3912-963d-204103818d34 | -3.60256 | -43.52043 | 2025-11-07 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c59b4af6-17fb-3fb4-b5ae-43cb1c02a259 | -5.77097 | -40.79657 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b64c742a-744c-3e9b-b82a-e21bd8a49b4c | -4.49479 | -45.92923 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a9e0b30-7db0-3238-9ca6-53f339ffbd38 | -2.83042 | -49.83232 | 2025-11-07 04:53:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8588b6b1-e4c8-3092-bca8-2b6ce047589a | -2.5076 | -48.26582 | 2025-11-07 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8a69b4-64ed-325c-a9b1-f1a577085f14 | -2.98084 | -52.82468 | 2025-11-07 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e9dcd5c-7a3e-3b87-ac45-f3eb7cd1a20b | -4.31447 | -55.84407 | 2025-11-07 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d98ac59a-6aab-36e0-b9f6-a710de27db4d | -5.37145 | -44.7326 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f08cf2e3-9066-37ff-a798-83511536fadb | -5.4659 | -44.89307 | 2025-11-07 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f073bc71-b268-39b7-b1fb-8dd545fae6d5 | -4.78676 | -48.64595 | 2025-11-07 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bdbb0c7-f28a-3051-a71b-8fc242ae4ec0 | -4.49041 | -45.92842 | 2025-11-07 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 811b1461-328f-3741-96d4-296593e0a1b7 | -5.77038 | -40.80087 | 2025-11-07 04:53:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README14.md)
