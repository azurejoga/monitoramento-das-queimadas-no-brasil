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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31398f0b-513d-3ec0-ba7e-4fa01eb050f8 | -10.78678 | -45.94057 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de5ba6b7-edfd-3e12-8391-b8a727746cc0 | -10.78797 | -45.93806 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 590a13d1-71d0-32d2-98eb-fc0be0bf3533 | -12.01034 | -61.84341 | 2026-09-11 05:29:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34a8b3c9-2d2c-30b9-9dcd-a34c8d5d570c | -13.25516 | -61.60102 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4a8a6037-675d-3c11-ad8d-c1a906598ef5 | -20.49627 | -57.46626 | 2026-09-11 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5846f745-bc54-3e94-9890-cda4d330b668 | -13.33916 | -61.66716 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e56f86-858f-3765-83f1-3eb265cf68d0 | -20.48837 | -57.46509 | 2026-09-11 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0650575b-d24a-38bd-9daa-783f027cb630 | -18.47948 | -51.7529 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ba2ff50-c30d-3e65-9657-3a4018bfd59f | -18.4799 | -51.74902 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9879f332-aff7-3d99-b514-9eba96de3fea | -13.31387 | -61.67405 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ede035-42a5-3db2-ac6f-3821d0e0a9f0 | -13.2236 | -61.62543 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63997a75-2ee2-3e19-bbdb-b1fe6047471c | -18.47926 | -51.74374 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d3d00ba-8d3a-3018-a447-3a3450ecdbe2 | -13.34529 | -61.67194 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f1fb70d-b5cc-3a86-b9f5-8eb4ea751aa0 | -13.32731 | -61.67633 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c71c623-3132-3ad1-9e3b-13f0652042eb | -13.31664 | -61.67824 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56b1cbdd-9a8f-3b38-ab7b-9f869d4f62a3 | -13.35142 | -61.6767 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7673a3d-145e-38dd-8139-97a00bbb7feb | -13.25793 | -61.60522 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 848c16d4-5d97-37c8-a5d5-64f12aaf0fb1 | -18.4735 | -51.75608 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cba4f107-2218-35f1-b04f-16aa27fb9d4f | -13.33067 | -61.6769 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a424e955-a4e3-36a8-9b09-0a2f06143145 | -18.4729 | -51.75082 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbfcfdb0-d1e0-3363-a21f-a8eb0dce718e | -13.21788 | -61.63936 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c97a9491-e540-33a3-8361-49c062c4597f | -13.29285 | -61.82384 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88198889-c5d4-3238-8838-91d36a4bb448 | -18.47887 | -51.74758 | 2026-09-11 05:31:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aa8fbd3-024c-336e-a954-e8e5cd159785 | -13.3279 | -61.67271 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 786ad35a-c6c3-322b-bb0e-4359cfe335f1 | -13.35201 | -61.67308 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0c53a06-916c-3229-8104-37ba7e19c42a | -13.25458 | -61.60464 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 29e9ce37-59ca-3ceb-843a-c6b94c915a18 | -13.2167 | -61.64661 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d5eab55-c9bf-3832-9bec-7ff22fa80513 | -18.48032 | -51.7452 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06abf9f6-a58a-34cc-9196-4b2487791e92 | -20.49232 | -57.46568 | 2026-09-11 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8e0c94a2-9735-3262-82f2-4185eb36fc51 | -20.48639 | -57.46344 | 2026-09-11 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ee31fd62-4248-323f-8151-18304d52c5b2 | -20.46339 | -57.45464 | 2026-09-11 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1ee6ee34-6b25-356f-a536-25c14d17a7a9 | -13.32 | -61.67881 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6fc6055-c926-356f-b6e4-32f6bd839048 | -13.34806 | -61.67614 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75e419f0-ac81-3f47-8066-20e51bd16eea | -13.33008 | -61.68053 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fcaabe0-14ee-3a19-b7fd-a8d7a3c2c656 | -13.34193 | -61.67136 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6331b09-7a91-33ba-83fc-313f753ef62e | -18.47848 | -51.75144 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13d4d694-d786-3278-b944-e1936170d857 | -18.47392 | -51.7522 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 934c23af-1011-38fb-8e32-aae0f87782e6 | -18.47964 | -51.73994 | 2026-09-11 05:31:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a777c58-cdcd-3347-b005-280d8774fa77 | -13.24509 | -61.59932 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6046c9d7-c806-30be-944a-23cd50b28dc8 | -13.21847 | -61.63573 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b036de6-410c-31de-a60d-37907895daee | -18.47808 | -51.75536 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e9181d4-b38c-3e27-b4b2-ea0ba0dda140 | -13.28948 | -61.82327 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c70359ad-e485-3f42-ae11-d16e4b992c97 | -13.21059 | -61.83265 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce92f5dd-16cf-361f-88a9-af21b688202e | -13.32672 | -61.67995 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47c3a139-fcd1-3980-93ed-6135bac24353 | -13.34865 | -61.6725 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01de8f7c-86d3-3d25-91b2-2d1d64e25441 | -13.22301 | -61.62906 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47abe1f0-f747-35f7-bf25-8ec5be73c346 | -13.22364 | -61.68881 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2d02b3e-65cf-3a65-84fc-93256127bd03 | -13.30379 | -61.67233 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1be15020-2d9d-3a89-a78a-6e79ac844f7b | -13.21336 | -61.83688 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 239f523e-746e-3f81-9d99-90549ec4ee58 | -13.34252 | -61.66774 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35e7a821-82df-3115-b55d-3c69d9f382af | -13.22418 | -61.62181 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e98efda-0582-3165-ae5f-ed2ee893b919 | -13.31723 | -61.67462 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6f8239-aba0-32f3-8c00-d13c38d7fc28 | -13.32336 | -61.67939 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187092df-afa0-37e4-ac72-1b7281dd80dd | -13.21965 | -61.62849 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd7c9bd2-bbb4-3286-ae0c-0ee4d64412b8 | -13.29622 | -61.82441 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb296d78-9213-3279-9c6e-bb38f37348e4 | -13.24845 | -61.59988 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9c552093-0e67-3074-bc49-57cb23f04f46 | -13.21674 | -61.83745 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d579fe8-3222-328d-8207-3e1971927a1c | -13.25181 | -61.60046 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 168e575f-ae1e-3f18-9e49-7434188b3672 | -13.227 | -61.68938 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4b22e30-44f8-3fc4-8417-78ca70354422 | -18.47252 | -51.75463 | 2026-09-11 05:31:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8036829-44a2-3e16-8370-84977d8776d3 | -20.48442 | -57.4645 | 2026-09-11 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2b40b4fe-6ff1-3ef1-842f-f712837207ec | -18.47433 | -51.74842 | 2026-09-11 05:31:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d0f7ba4-17d6-30f4-9961-60e47fa20a50 | -13.21906 | -61.63211 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 641777bd-a89a-32d1-9163-22fde4e5c0f0 | -13.34311 | -61.66411 | 2026-09-11 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd284c1b-04da-3572-83ed-356a2107560c | -13.21729 | -61.64298 | 2026-09-11 05:31:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 857cf186-e40d-32b9-a7f9-30b0403c6393 | -18.47474 | -51.74463 | 2026-09-11 05:31:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f59d5508-d3cc-3c04-bd10-4604b38d7e24 | -22.27857 | -55.8446 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c5f91d5-93bf-3247-9042-79e3f62f60d8 | -22.27273 | -55.83598 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99247919-17aa-3016-ab7f-4d684e25b083 | -22.27074 | -55.83382 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 188fc83b-b725-3126-8b0f-325cb49fcf25 | -22.26515 | -55.84269 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8af7fa9-4d75-3878-abe5-fd771583f742 | -22.26068 | -55.84203 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c59e87a-7768-3396-8876-184cc3b8d3d9 | -22.27018 | -55.83863 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4425bf26-1773-34d9-a063-2e553c03bf50 | -22.27409 | -55.84397 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e62015c8-8444-3617-80fc-4df0f0b7aa05 | -22.26571 | -55.83795 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae61f8b9-c035-3085-bde0-954697b5bba6 | -22.26906 | -55.84806 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bd4ad60-9a10-3de4-9459-0877241c9500 | -22.27668 | -55.84136 | 2026-09-11 05:33:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd7ba5bc-effd-33bd-a246-656c2c1fb406 | -9.50969 | -40.33339 | 2026-09-11 05:38:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 762d57ec-c193-3309-8219-2e208b4818cd | -9.50083 | -40.32701 | 2026-09-11 05:38:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| f83eb4be-7a35-3d56-990a-ff81a784501c | -9.1799 | -68.2194 | 2026-09-11 05:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| caa4af45-fdc6-33af-b1f9-4086ff12b8ea | 0.30394 | -60.44027 | 2026-09-11 05:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e46f84c-1c4e-3525-8e9a-a68af327ea92 | 4.21218 | -61.11244 | 2026-09-11 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 115d6b61-d482-3675-bf1b-8c172e5850f4 | 4.49599 | -60.85028 | 2026-09-11 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 379ff876-3000-3fcd-b73d-dd7d2595b371 | 1.28589 | -50.68567 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 706b1595-2788-3697-a366-980f8ca21d12 | 2.49212 | -50.99303 | 2026-09-11 05:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a789e483-3ce9-3857-8a3a-7a1b3074d6cd | 1.29169 | -50.67469 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a4ecfff-f1d5-35c6-b2ed-e89fdd590cbe | -1.02904 | -53.73768 | 2026-09-11 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 136af81d-b106-3167-ad13-010858e8014c | -3.0747 | -51.33876 | 2026-09-11 05:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33286903-9b34-3782-8c68-e15a70c0fa31 | 2.60719 | -61.42891 | 2026-09-11 05:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1b4731f-ebc2-39c7-888f-2fd82ddf0e1a | 2.49749 | -50.99557 | 2026-09-11 05:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e47da2-af49-3f10-be3b-1e572f1399a0 | -3.06771 | -51.33764 | 2026-09-11 05:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 16ee66a1-c366-3108-bac1-bf0c64840259 | 3.40798 | -60.89121 | 2026-09-11 05:46:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98afdaac-65f2-347a-af0d-95bfc07a5386 | 1.29171 | -50.67823 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa8c188a-74b9-335f-8ed4-3f696e314670 | 2.51446 | -50.85679 | 2026-09-11 05:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f8e3bfbd-e1f0-3554-9bb6-ca502a3d8b13 | 2.51245 | -50.8451 | 2026-09-11 05:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19a430d4-48fe-331c-859d-6a40606d994e | 0.11616 | -60.62453 | 2026-09-11 05:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4968f1e-b1f5-3384-ac51-316debe64eb6 | -3.06946 | -51.33782 | 2026-09-11 05:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef43f3e2-ddf9-3a54-8969-5e281be964f0 | -1.02846 | -53.74147 | 2026-09-11 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ffe75cc-6e5f-361b-888e-d3b3c83ecab2 | 1.2859 | -50.68208 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43bf5443-fc0d-3b64-8c74-bc42b77460a5 | 1.28012 | -50.68949 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8d4ced0-618d-3401-867e-b08c8cd7d2a8 | 0.11982 | -60.62397 | 2026-09-11 05:46:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README31.md)
