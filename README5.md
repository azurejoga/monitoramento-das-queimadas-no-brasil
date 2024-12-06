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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24a670c7-3ac2-3e8a-a73e-005b748c78a6 | -6.26749 | -46.91852 | 2024-12-06 04:50:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e13f375f-5bd0-3ab8-a0c0-94c1f0cb85c7 | -1.74873 | -52.80769 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 126a9a4a-5ddb-334a-919e-9cf2ccc3ac34 | -3.12156 | -53.99202 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec38a13d-3b3c-3dd4-8c6b-c739e6d9706f | -2.38241 | -53.7065 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a51b25b-0c5e-3bf1-9a03-014cc801745a | -1.8923 | -52.8482 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9997c323-e831-3969-95d3-942a182f950a | 3.23964 | -61.03241 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91156de8-5771-3ab1-836c-196a231bfa76 | -1.87992 | -53.30404 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7be60c80-f511-3e7d-bdf0-beddf13c914e | -3.39996 | -42.2975 | 2024-12-06 04:50:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaad025f-3032-37de-a95c-01eac3431e30 | -2.60591 | -54.2317 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a81e6f55-110a-3884-b944-acc84f6b6159 | 3.23136 | -61.03616 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae4973fa-274d-3347-b383-f3944107ed81 | -2.38081 | -53.94977 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 272e9f86-038a-3fe6-b1e3-3cfa88f85af3 | -6.92788 | -42.82922 | 2024-12-06 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fc66820-a27b-30b4-b683-05c406c6389d | -5.21132 | -44.65402 | 2024-12-06 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2791fecf-6d0a-39f6-8857-3b37d2b53bc7 | -7.22791 | -39.95675 | 2024-12-06 04:50:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 04aafa16-e917-3adb-896f-f94a1695e9b7 | -3.12217 | -53.98825 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eff543a5-404d-3c34-a78f-71a00907ee3e | -3.81991 | -54.76162 | 2024-12-06 04:50:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6961ab27-2fce-3a75-8ed4-8a4b552b51dd | -1.90116 | -52.88574 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e7ad2f8-2100-3b91-9e30-4c46f400e6f0 | -3.40003 | -42.30231 | 2024-12-06 04:50:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d00c72bc-75a2-3b5b-9334-218b89d4741e | -1.47116 | -52.68457 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 080b821a-95e1-3820-bc2e-acb52b20a888 | -3.11812 | -54.05737 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5a47de-1e0a-3137-8bcd-417109828ae6 | -6.78384 | -40.22561 | 2024-12-06 04:50:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e4643ca-31ef-3140-9a26-81abebf909a9 | -3.17791 | -54.33361 | 2024-12-06 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9527dbf-1d54-3eaa-9f03-e3b78f57ce18 | -1.59313 | -52.7802 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36a77822-aba5-3861-ad83-26b7ccd1c22a | -1.70123 | -52.59754 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6073d05-4dda-331c-a757-1141afbe1a40 | -4.13002 | -54.89924 | 2024-12-06 04:50:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81264ab3-6c07-335f-a2ab-58e8b3ab62f5 | -2.74402 | -54.15756 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afd32a66-3bd5-36a9-9cf9-0134a1bb7509 | 0.75254 | -59.65781 | 2024-12-06 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcdeeb00-d408-38b2-89c0-388244927578 | -1.66667 | -52.75163 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5a8e7e7-9436-3b6f-9b6c-26f58faa0102 | -1.78517 | -52.75152 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60d8c54e-1f00-38c5-b307-e91abc80d86c | 3.23727 | -61.03522 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94d609c3-f468-3e54-91a9-731a0a9f6623 | 2.4298 | -60.64962 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0751fbe-6366-3dde-b061-e1b8fc2b2841 | -1.78461 | -52.75507 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff9ae92a-436c-387e-a8c2-5236cb431454 | -3.10995 | -54.06388 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 923802f0-8930-36f2-88a3-3fadb1dfcb50 | -1.67115 | -52.74506 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e05d4903-c776-3aa6-9c80-5e306eaa6f12 | -2.60942 | -54.23229 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccd7f76c-6c82-39c5-b09b-d63027fa8810 | -1.69225 | -52.56726 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d686e786-3c9e-38c1-914b-808b837a1490 | -2.46784 | -53.71575 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a03e5b3-e79b-3dc8-9bbb-4ec9be5067b8 | -1.8104 | -52.73353 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60d4b3b9-3890-3c4b-beb4-7bd166b54e18 | -2.5261 | -54.05428 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0ebcf0b-aebc-3015-8861-3a138bd53fde | -1.95018 | -51.20556 | 2024-12-06 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a13947e-7047-3a8b-8d4c-965158e495d5 | -3.21123 | -53.94093 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db0340e-99f5-37fe-aecf-2a62192050f7 | -1.68577 | -52.78375 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee8ea5e5-c9ca-3f7e-9f81-dd32a8655df3 | -1.90048 | -52.62093 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5582e24-6a47-378a-b8b6-b30084f4d8ad | -1.67214 | -52.56412 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a0449a4-8c4e-3db1-a04a-4e3c5e3c5729 | -6.45646 | -46.34186 | 2024-12-06 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95e9cede-a933-3710-a0b3-bcf00a491d74 | -3.26722 | -53.86811 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5e0b770-b2e2-309d-9df8-9b7d010a8095 | -1.6956 | -52.56779 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c3752d7-d8ef-384c-81d3-8cc2f54f61b7 | -6.45645 | -46.34369 | 2024-12-06 04:50:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee8b6320-e3b1-3e6b-a7fe-5198a3bfb4d6 | -1.90065 | -52.84552 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37c2884-7111-38e9-b33a-37c573939838 | -2.37778 | -53.71347 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e085d2c9-dc3f-37ef-a27c-fee9ca593cee | -1.70383 | -52.7861 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a1ce3cc-c60c-304f-ac23-3cb1214ffac0 | -3.21064 | -53.9446 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5093b0b1-9076-36a9-9215-fa335ae59d7e | -1.87651 | -53.3035 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70fb8d0-07a3-3b75-858d-cbc3fa9b627a | -3.09484 | -54.05827 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69a3002-964c-39a0-a7a5-22b836aaf160 | -1.89768 | -52.61689 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 214af5f7-41d6-30e1-8fee-3ab733e94a28 | -6.56995 | -46.75974 | 2024-12-06 04:50:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30c3ae17-a0a6-3482-b882-c84c99fcb498 | -3.24132 | -54.0956 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee87d79-7aec-3d86-b164-cd21af3860f5 | 2.62357 | -60.40908 | 2024-12-06 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f11d7ba8-7fb3-3f42-a73b-320d4b72bfa8 | 0.75303 | -59.66094 | 2024-12-06 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c852b19-439e-32df-bf82-850b08c2f48c | -5.14629 | -49.63233 | 2024-12-06 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c5ad2e-504b-31ae-9430-c32882e2bf70 | -1.81376 | -52.73406 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 681d01ce-bd28-3c98-b361-e2f14e0399f0 | -2.60742 | -54.04227 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c93cba2-7ae6-3d1b-ba68-f514420fcddd | -1.4678 | -52.68404 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f49c621-24b0-3f3b-a1e0-b0079b755972 | -1.90346 | -52.8496 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9085cfa0-00e0-3ff7-a326-e4ab9e48698b | -3.68952 | -54.3128 | 2024-12-06 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0da7bfe2-ac04-35c4-b176-68ae1cedbbdc | -3.83616 | -54.6827 | 2024-12-06 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2dc67af2-6482-30bc-ad4a-8071f133d14e | -1.89712 | -52.6204 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04c7ee40-630c-34bf-81c5-3652ade6a7bd | -3.10648 | -54.06334 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76b60235-07b4-39ad-8bb2-3f2cae6e402a | -1.81659 | -52.69462 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbcc8cdc-b823-312c-8007-84be50266793 | -1.6633 | -52.75111 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7a88d2-b3ce-3854-832d-ec8316f4fdd2 | -3.11342 | -54.06443 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30dfe55d-c99d-3a73-9b34-1ac899a632da | -1.90172 | -52.88217 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 470967a1-9fde-36e9-ae3d-b7957e908e53 | -1.6824 | -52.78323 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 346d3ab8-a576-3c49-b267-290d2d538bf4 | -1.79134 | -52.75612 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d6a5718-c78c-3861-9d6a-594dc8bc9eb3 | 3.23667 | -61.03103 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bcc57597-0d7b-3535-9472-2bd49b8dee20 | -1.67995 | -52.55813 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f8c9236-31e4-3fe1-9b2a-f3ac49b77cf5 | -1.67549 | -52.56464 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fb47f60d-2b6d-3d4d-927f-54bf7dfa0b6b | -5.74292 | -46.65381 | 2024-12-06 04:50:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f3c682d-8732-3077-b392-3c51d893b228 | -1.87708 | -53.29985 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a478571-88f2-3ebb-9af2-9f71bdeed9c6 | -2.28747 | -53.79149 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f20bf05-2f63-3b56-bfc7-b9266516d44d | -1.66779 | -52.74453 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce21df00-37ce-36a0-a757-49fcf56e5b4f | -2.68235 | -54.67397 | 2024-12-06 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c61b5c35-eb2a-3ca9-a92b-756f670f017f | -1.90682 | -52.85012 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26b60d48-02b9-3541-9025-886866d18f2b | -1.66274 | -52.75466 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 558cdcde-f112-3a32-bc7e-ac152d08a414 | -1.70663 | -52.79018 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01184b8-5b38-3120-946a-3dc4ce3d9702 | -1.66723 | -52.74808 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a2e6da7-c2f7-30d7-b70d-22c147ccd5ea | -1.93468 | -53.13378 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd7b7bfc-66e5-3b18-8572-e8b1b2d99329 | -1.67003 | -52.75216 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c57aea56-0414-3ef1-bda2-d9a83471823f | -1.53561 | -52.67618 | 2024-12-06 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ede9e848-df70-30de-bda9-470dbe282bc5 | -2.49597 | -54.10866 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ab157a8-95c4-325d-87a9-f3820abcaf57 | -1.73132 | -52.80861 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b4493e3-3e92-35cb-9647-0befcc324af5 | -3.17728 | -54.33749 | 2024-12-06 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b417e747-de47-3d36-8d3e-54932af0aa3b | -1.68051 | -52.55462 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26d1742-6653-3ac6-befe-68a2c09cd2f5 | -2.5507 | -54.03432 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba73f3d-ead2-37de-b9df-3f090427b6c9 | 3.239 | -61.0282 | 2024-12-06 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e4ce9c7-e85a-335e-9d18-9ed0fc268e3e | -2.40394 | -53.80584 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c616113d-e369-3446-9427-51f06240fb42 | -3.10119 | -54.06314 | 2024-12-06 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 678290f2-c7db-30dc-856c-7cc228bcac1e | -1.78798 | -52.7556 | 2024-12-06 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03abb71b-1ec8-3b16-91eb-4d1ab901641e | -2.25754 | -53.81082 | 2024-12-06 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9918893c-b79c-3524-be8b-2248adade050 | -2.61292 | -54.23287 | 2024-12-06 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
