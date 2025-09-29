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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ebb6b76-cf1b-3e75-8229-1365e9bdd82f | -6.035 | -43.93084 | 2025-09-29 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 61f24686-3119-3802-9779-e4e35772a2a2 | -6.75921 | -44.7456 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5708352e-f553-3190-a310-2ce20e3c59ca | -8.27925 | -45.52606 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fc1beb89-b2ca-3b51-a11b-71fd9e833c79 | -7.489 | -44.29876 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7bddfc0a-4709-3529-b7c6-f0f46768d5e7 | -8.51935 | -47.85265 | 2025-09-29 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5c1ef5b7-65ec-3f57-b7d8-6893e8ac1d00 | -6.76442 | -47.10703 | 2025-09-29 12:17:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cec1333d-3f5c-3f71-902c-cd882905aa05 | -6.46118 | -45.1533 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 784fcaa3-816a-3dc4-8a52-191c2ab4ff1c | -4.6639 | -46.44734 | 2025-09-29 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a182533c-714b-3a70-b51f-6574db798843 | -6.56812 | -43.40545 | 2025-09-29 12:17:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8d6fc888-cb4f-357f-940d-759247e1c6cf | -8.88728 | -51.65414 | 2025-09-29 12:17:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 699cf480-2d58-3f00-bbd4-4f5fab7d9df6 | -8.04553 | -47.17646 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 59cb0a4c-f218-3f37-9862-9fe701027e23 | -3.39685 | -47.49485 | 2025-09-29 12:17:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0cdeee16-dfe0-3bfd-8573-3fdb9ab3d51f | -7.98095 | -47.31197 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2332e73b-33ce-3047-bcb1-4e6cf182cc14 | -7.51821 | -44.30258 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8701972f-cc01-3186-9229-ca65e16fc33d | -5.7239 | -43.96908 | 2025-09-29 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| dfa27d25-b558-3149-bbb5-3892dc3c77c0 | -7.81368 | -46.98974 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| cb9e69d7-9095-3f2f-9531-f8954904b332 | -6.15336 | -43.88586 | 2025-09-29 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6a811724-2bcc-39d1-ba3f-84ec65865fcc | -8.28325 | -45.4973 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 3c163ac5-5bd8-381f-ad63-728b21248b46 | -7.23075 | -44.77481 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 28642b26-8430-35d5-8f54-368cbf7d20e3 | -2.80623 | -48.62238 | 2025-09-29 12:17:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f66a98f9-517f-3269-bd62-8bf85375bb7a | -4.3167 | -48.08307 | 2025-09-29 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 581834e3-bdfc-3a4d-83bd-e31d79548f40 | -7.80998 | -46.88971 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75c2a150-b6e7-3713-9332-f9503a574548 | -9.46081 | -45.49959 | 2025-09-29 12:17:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36bdcf30-19d6-38b7-a447-c036b594a5f1 | -7.8556 | -46.76021 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 473bf21d-8263-33ec-894c-3437f2cea66d | -6.64627 | -41.39683 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| cf1711cc-8b03-32bc-8dd7-9eadae2ec8b6 | -2.91708 | -48.19524 | 2025-09-29 12:17:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 894e4a97-ff9a-325e-8429-959875d39ad2 | -7.43663 | -46.984 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 39d0d1c7-3481-3395-80f8-aed498700739 | -6.2606 | -43.63284 | 2025-09-29 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4432fad8-63cd-30bd-a4d6-06cf41fc9a85 | -7.81241 | -46.9986 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1800df99-37e4-37b0-9652-600f24c86145 | -6.45986 | -45.16283 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a760fb7-4c3c-34f9-aaf4-3de2a61a2bc2 | -8.88441 | -47.62958 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ff3b71dc-dbab-3747-85a3-d4caf951ffb0 | -9.28224 | -45.73188 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 56569619-c6fa-3efd-a74e-75b4e53da311 | -6.08233 | -44.70212 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 96033ee9-b658-3293-a78e-bec54d9554c3 | -7.84802 | -46.75007 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 36652ee0-ab52-37dc-93aa-68a0b3597d1c | -9.07771 | -45.87701 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2bf20af1-450b-359d-932d-cd6f300983c5 | -5.90412 | -42.48925 | 2025-09-29 12:17:00 | TERRA_M-T | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| f69dab70-2bdf-316e-b38e-4826fcaf0c00 | -5.19073 | -43.7604 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| e29c162f-93ce-3410-8d76-c10404d1049b | -4.66516 | -46.43855 | 2025-09-29 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 184f0681-69d9-3a94-9724-20706c125e53 | -4.5565 | -46.67753 | 2025-09-29 12:17:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b2014c94-c1e7-3610-b61f-27f73fade46c | -7.47066 | -46.29189 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3af1d703-d56e-3ecc-b699-f43c08647a69 | -5.35525 | -43.68333 | 2025-09-29 12:17:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f8d7e2d0-831c-399a-9b6a-4614d41f03a3 | -7.55378 | -46.29146 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7fd0a648-f27d-329a-a35a-b4a6d84937ad | -8.01915 | -47.04615 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3cfe7cbc-e6c6-33cf-bd78-ae2298feb320 | -8.28706 | -45.53716 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7af03b48-d00d-38d6-a46d-abf6ae61e45a | -7.13142 | -45.49791 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 876251f1-1d06-38c2-bde9-cdae37f01252 | -7.89781 | -44.60302 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e1ffd160-9da0-3af9-969d-63af5d3b489d | -7.84997 | -47.25386 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 74a1fc87-a6a5-3b20-9ea7-4ee9ad2fff29 | -6.07926 | -42.46959 | 2025-09-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 6ec58723-c2ae-3b07-a537-9c41617258b8 | -8.26871 | -45.53448 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9ff2e936-664d-371a-8b14-8dba3fb8c7eb | -9.44181 | -47.60125 | 2025-09-29 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 782fb45b-b9fd-3bbf-8964-a9d9885edf1d | -5.58846 | -44.35096 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 043310ba-891f-3eca-b4a5-09aefc6db666 | -6.0748 | -42.47713 | 2025-09-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 98b701ca-1230-3578-a565-026dc884a377 | -7.61002 | -46.60696 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3a9c7a8-5009-3556-a780-5a72a7f8c02c | -8.23384 | -47.53878 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c862d08a-e7d7-3bc4-bca9-362d79976f49 | -5.2005 | -43.76172 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b3e6b81f-e06d-3465-9ee9-c094ed419980 | -4.71034 | -41.97584 | 2025-09-29 12:17:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| e003f25e-618e-3c20-93c0-3b87aaafe24c | -6.9766 | -43.77712 | 2025-09-29 12:17:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 0711b46e-ff34-38e5-9512-a4018b70a1a0 | -8.82156 | -46.19205 | 2025-09-29 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 91f23776-8081-3408-94a4-58749856ff62 | -7.82252 | -46.99099 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c1d0669c-7f91-304f-be10-0f2bb8bdaac2 | -9.31539 | -45.68333 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2ad4e5f2-ac5c-3bdf-9457-24454231dc89 | -6.62412 | -45.89759 | 2025-09-29 12:17:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5e019d92-a8b0-3a41-994b-5a20664669cf | -8.68669 | -48.29104 | 2025-09-29 12:17:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 43965a63-4988-308b-883a-b6d34416c55f | -3.09764 | -47.01223 | 2025-09-29 12:17:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 66f49445-2715-3e87-9b27-f031a79a6d2f | -9.66284 | -45.83466 | 2025-09-29 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e1c28cae-7368-3ff2-a331-921444552c16 | -6.09894 | -42.65047 | 2025-09-29 12:17:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| fe273448-d4b7-3be2-b4a5-bf843a879790 | -3.3766 | -43.12541 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 501b2004-1b3d-31bf-9466-e74f7767ae16 | -6.42814 | -43.08737 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cd37794f-158e-3933-9e17-f70da358f33b | -3.45308 | -44.13239 | 2025-09-29 12:17:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 62422d5e-52cd-3e86-8082-8f7e88a70800 | -7.89336 | -44.6069 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 0e64f275-433e-3af1-8a31-dde00c98988e | -7.97968 | -47.32083 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| e3550349-7f06-3843-81dd-82b176479be0 | -8.82026 | -46.20129 | 2025-09-29 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b824d102-232e-396b-b030-d6b5f13bd831 | -5.98023 | -45.36462 | 2025-09-29 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6cf9aa89-510c-3d46-9d50-98d708668de5 | -8.68536 | -48.30014 | 2025-09-29 12:17:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dc590d7e-4286-3b08-91a1-06a1326a0768 | -6.29093 | -45.25331 | 2025-09-29 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b7e1b8f4-a15b-388d-b13a-7ca93d481b8a | -7.24517 | -43.00317 | 2025-09-29 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 96623d4b-aeff-3230-a274-16ef68b343bc | -6.12833 | -44.44095 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a893b4a7-99fe-3c98-9f64-9d50f0577cd8 | -7.80871 | -46.89859 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 48ceafbf-4b68-3d19-a779-bb3530937eb6 | -6.4162 | -45.15062 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1605c65e-3804-3dff-81ce-516cff1d616a | -7.71174 | -46.80605 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7b394413-bd3e-3820-b308-da5939250f62 | -3.32161 | -48.71624 | 2025-09-29 12:17:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6915add8-25a1-3a9d-99ba-1cb283792ddf | -5.89806 | -47.67972 | 2025-09-29 12:17:00 | TERRA_M-T | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d55d93b4-9fa3-393e-87d3-0e8e16a0e959 | -7.28186 | -45.80703 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| dcb08a91-b02f-3d1a-9f21-fd8f6ec04f76 | -8.2884 | -45.52755 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 1e991e02-be3d-383a-aa6a-7045e9d5be73 | -7.90067 | -44.58176 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7456e31b-0b86-34cd-9064-f3a5ec8668cc | -4.96801 | -44.49574 | 2025-09-29 12:17:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4c358e4f-820b-34fd-bb32-2d412e39f5e9 | -8.25794 | -47.49689 | 2025-09-29 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3b452d7a-cd20-3a9f-999f-5b3f39d34a8b | -8.44302 | -46.91338 | 2025-09-29 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1ab2300e-ae48-3e64-820c-42717498766e | -9.14743 | -47.78601 | 2025-09-29 12:17:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6d0c9a5b-878e-3ad0-9f7a-df2e73514f3e | -7.46937 | -46.3009 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| cfa1b692-fc36-3e44-a193-2cc1923a4616 | -8.52496 | -44.62715 | 2025-09-29 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5249fcca-9a01-3829-ac8c-934d4efd4e33 | -6.07212 | -42.60631 | 2025-09-29 12:17:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| bd18a595-66e2-3c5c-ac57-c087019486a1 | -3.78616 | -38.64142 | 2025-09-29 12:17:00 | TERRA_M-T | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 49.7 |
| bc92cd9f-0214-3a6f-a58a-34530c302e5d | -7.89927 | -44.59216 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 08d96355-5a31-3ac5-b2b0-306a8089a113 | -5.35272 | -43.68821 | 2025-09-29 12:17:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 24083f35-cd27-32ed-bf4c-0404b7b63fba | -2.25163 | -47.89231 | 2025-09-29 12:17:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 08a33784-607e-3da0-adbc-044ba4e9904f | -7.81997 | -47.0087 | 2025-09-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c0a72d65-4b15-3879-af57-0d96bb952fc8 | -7.89637 | -44.61377 | 2025-09-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0551dc19-6090-371a-9e4e-277b7b7aa686 | -7.22936 | -44.78499 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 09e5b25b-3e16-3ecb-8872-16fea895b814 | -8.28974 | -45.51796 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6fb0979a-64dc-30cc-a4b1-e98127ab1f37 | -6.07672 | -42.46332 | 2025-09-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |


[Clique aqui para ver as próximas entradas](README84.md)
