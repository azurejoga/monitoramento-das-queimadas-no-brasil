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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e41108a1-d445-3c01-a4d6-7aab512feb67 | -8.6696 | -46.3842 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| af8d99ed-9eae-3be0-aa7f-dd9758d13a65 | -6.381 | -44.3975 | 2025-09-16 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 02acde32-9d07-3fde-bc93-cc5edfc2743e | -11.1299 | -45.3426 | 2025-09-16 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d181892f-429c-3180-9bac-1430f5038a4e | -14.6143 | -46.3806 | 2025-09-16 13:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| b3429b99-1a6e-3ec5-bf5d-0957543d6136 | -15.9996 | -59.2647 | 2025-09-16 13:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 27231fc8-6949-313b-aed9-7b841f3d53c4 | -14.1641 | -54.0613 | 2025-09-16 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| c2ceb76d-5be7-31c9-ace0-ea0d0b2e1c26 | -6.356 | -43.1476 | 2025-09-16 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 46f0a8de-c46b-35f5-aa03-eefb6ca35f5e | -6.362 | -44.422 | 2025-09-16 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 607bac37-308f-3a80-b31c-76b62530c124 | -9.1709 | -46.9792 | 2025-09-16 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| ed1c7590-ef5e-3e98-8695-e523ae6daef5 | -4.5934 | -43.3239 | 2025-09-16 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9c0204e8-e66d-3ed3-90da-7ec8d6cf769f | -6.6698 | -45.5118 | 2025-09-16 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d7950934-e554-3e71-a2bc-a2a72d908ee4 | -7.6949 | -44.486 | 2025-09-16 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 5bd29564-3443-3555-8ef8-020227e67275 | -8.0196 | -45.662 | 2025-09-16 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 354.2 |
| 1111c9f5-c1e8-30f8-bb7e-d61cadc63d6a | -8.6885 | -46.3823 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a479bead-48bd-3163-8943-0d7aabf88e64 | -8.9592 | -45.8591 | 2025-09-16 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 50211d84-a230-3e7b-9a97-27b9785752f4 | -10.9004 | -47.8027 | 2025-09-16 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8d7f9221-e22e-3159-955b-991f049d3a71 | -7.078 | -44.153 | 2025-09-16 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a673b356-c007-3925-a917-ca40564dc60d | -7.6949 | -44.486 | 2025-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 224.9 |
| a8e972f6-d17c-3091-b31b-7da2d4f646b3 | -14.1727 | -46.1354 | 2025-09-16 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f8046507-124b-3500-a27c-295e4d15ae86 | -14.1641 | -54.0613 | 2025-09-16 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| e530bcdd-4d9f-3b89-8dc9-3dea186a8618 | -7.9822 | -45.643 | 2025-09-16 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 8fba7e00-ee3e-3524-82d6-1e37bc56a0b8 | -11.4853 | -43.5929 | 2025-09-16 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a29fed29-d71e-3684-9104-77ce1536404d | -7.6738 | -44.6717 | 2025-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| dc7f64c0-24f0-32d2-99e2-54aa7deb19a2 | -8.001 | -45.6412 | 2025-09-16 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 441d7498-020e-3392-bdc2-7b55f105c828 | -7.5269 | -44.3644 | 2025-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6f1ef87a-e961-32e8-8be8-543a519abd22 | -8.0007 | -45.6638 | 2025-09-16 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 209.8 |
| cdb47357-05bf-35e1-a556-79effafef7ba | -5.8086 | -43.4956 | 2025-09-16 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 1b6818d2-97fd-34ab-ab09-491b74238e88 | -13.2027 | -47.3126 | 2025-09-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0de82be5-18e1-357a-ac3a-3fdd75f60ae2 | -8.9731 | -46.2405 | 2025-09-16 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 585.1 |
| 158dcf4c-908e-3868-8a4b-72698b8f07a7 | -8.6127 | -46.4124 | 2025-09-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6c643e61-49a7-3572-b922-0a33119a8f47 | -11.5041 | -43.6136 | 2025-09-16 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ad4352fd-5108-37ed-89fb-5595769144a7 | -12.6352 | -45.7652 | 2025-09-16 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| de52583c-515d-3505-bfe9-883ca6cc8d15 | -6.8343 | -47.8284 | 2025-09-16 13:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 9e474629-f62b-334e-9a11-7d3779cded6b | -15.752 | -49.76 | 2025-09-16 13:20:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e367da1c-a460-3135-bb62-025b021291ce | -7.676 | -44.4879 | 2025-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f97216d4-75be-39ab-b00b-e973f673d9d8 | -6.1881 | -41.1855 | 2025-09-16 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| b4869d38-d652-307d-bf98-55de13ca07b4 | -9.1523 | -46.9589 | 2025-09-16 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 236dc6ca-2c39-3ffc-bb60-5ef36d738eb1 | -6.1878 | -41.2097 | 2025-09-16 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 69129ed9-5650-3ee4-94fb-34e4bd843e83 | -10.7493 | -46.5058 | 2025-09-16 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5f9376d3-e123-3ced-b688-c7a4876c8874 | -12.6356 | -45.7422 | 2025-09-16 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3dcc2487-4f5d-3514-8c50-64c3099e0519 | -7.6763 | -44.4649 | 2025-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 2dcacb62-b628-3d1d-9117-ef8484388069 | -10.7299 | -46.5307 | 2025-09-16 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 203.1 |
| b97efcdf-cf59-3f7a-bdf2-d2dad14cc0a8 | -6.8156 | -47.8298 | 2025-09-16 13:20:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c209c26a-94c3-3d75-ac22-326321e34ca9 | -5.9942 | -43.6902 | 2025-09-16 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 605ab678-9d34-32e8-aed5-843f6c91019d | -6.337 | -43.1727 | 2025-09-16 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 701a7a03-5ecb-3af1-b92e-6a0ed2db6dda | -7.2768 | -46.6036 | 2025-09-16 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 155.0 |
| f56769d1-0d7d-3dde-ac0c-fbb054af22fa | -13.2798 | -54.2435 | 2025-09-16 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f76fdee9-09c7-347a-9df2-51cf8e2a1510 | -10.7302 | -46.5082 | 2025-09-16 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 6345de22-ae51-35f2-a647-39105ccab038 | -9.152 | -46.9812 | 2025-09-16 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| eb94bf43-fc55-36ca-93a6-d13421f03e74 | -14.6143 | -46.3806 | 2025-09-16 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9c418551-49f1-35fe-a488-e10b4beb47b7 | -7.2581 | -46.6052 | 2025-09-16 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 01b51b5e-9f92-35df-9c3e-ced9440571a3 | -15.5341 | -48.0381 | 2025-09-16 13:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 130a2a45-28b8-372e-ace5-f4079a9d6346 | -9.1709 | -46.9792 | 2025-09-16 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 53920e69-ac37-3133-8e20-9bf9b16f6215 | -6.1693 | -41.1872 | 2025-09-16 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| b61f76cd-5c9e-3f3b-8b0c-960817611636 | -8.6699 | -46.3618 | 2025-09-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 947fffb5-48ff-3119-8ad6-d02ed8f4e179 | -11.1299 | -45.3426 | 2025-09-16 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1f1277c3-5c61-3494-aaaf-aa631a2ea524 | -7.2771 | -46.5814 | 2025-09-16 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 4e5e5c76-7153-3038-9865-4321c879abba | -3.8416 | -44.0824 | 2025-09-16 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 546.7 |
| a7f33931-b0d3-3199-b87f-d912ae657f8d | -10.7489 | -46.5283 | 2025-09-16 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| cc3a7372-bcbf-351d-bddf-b17ce40e5489 | -15.9996 | -59.2647 | 2025-09-16 13:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 61637847-37f9-31a9-8453-d188cb4a55b2 | -8.9412 | -45.7933 | 2025-09-16 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 10087cbd-8a2d-3601-9f4d-7217e6962e98 | -12.8087 | -44.744 | 2025-09-16 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| e1711b8e-9844-3a38-8d7f-a6b19c35b55f | -8.613 | -46.39 | 2025-09-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 25e73f36-3f05-386c-8fd7-5025c9da8c12 | -6.3558 | -43.1711 | 2025-09-16 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| b909d9e1-feaa-3e33-87fc-aa1b82c4bf52 | -12.8404 | -47.1417 | 2025-09-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 83ac9029-5cc9-3265-9bd0-3ce3907b0e6f | -6.169 | -41.2114 | 2025-09-16 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 275c8e06-22e3-3e7b-b21d-6e5d258e9d49 | -10.9671 | -47.1729 | 2025-09-16 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 98f9a2e4-4d0b-3306-8773-20e74c63b9e6 | -8.0005 | -45.6864 | 2025-09-16 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f2108920-9a7d-3cf0-a1f4-23b9c28af76f | -10.802 | -50.6965 | 2025-09-16 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1edc77ad-7344-341f-85ec-5a3eff34c700 | -5.8088 | -43.4724 | 2025-09-16 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 57b68c70-7f3e-303f-a7e6-f82bcf119fe5 | -7.2956 | -46.602 | 2025-09-16 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 3886c40b-72c1-35fd-9fd1-ef47a8d9ed44 | -13.2801 | -54.2228 | 2025-09-16 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 16116bd3-c06b-3c52-a843-afdd650750bc | -8.0196 | -45.662 | 2025-09-16 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 392.3 |
| 05319c45-ccf8-33d6-b3df-eb5f9558c3ca | -9.1712 | -46.9569 | 2025-09-16 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| afa46034-83bf-39bf-92e2-0625ce703d5c | -6.3372 | -43.1492 | 2025-09-16 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 69bdb68f-9b85-3035-890a-8ba233986892 | -6.356 | -43.1476 | 2025-09-16 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 361.2 |
| 5ea41608-0455-3f81-a0ce-e6cffeac8066 | -8.6696 | -46.3842 | 2025-09-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 21e672e1-48d4-35f8-9395-f6e7dcb32abc | -11.4849 | -43.6166 | 2025-09-16 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| b51d33f2-2fc6-3d2a-8201-e4dab32f6ae0 | -7.6927 | -44.6699 | 2025-09-16 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f2a3d649-2088-30f4-9cae-c45fedfd18d0 | -8.9259 | -45.5231 | 2025-09-16 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| d517c64f-8ce9-38c1-977e-6d51eaf07fff | -8.9728 | -46.263 | 2025-09-16 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 9f9afc5a-3253-374c-8f06-4ed11083de26 | -11.0804 | -49.7456 | 2025-09-16 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 26f0b51e-0304-3aa2-a3b3-7f2a1a667eea | -12.8409 | -47.1191 | 2025-09-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3db8072b-609f-32d1-a758-2f76f228e10f | -8.9734 | -46.218 | 2025-09-16 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 70253fed-dbc5-3770-8f6b-494041cfbcfa | -5.8088 | -43.4724 | 2025-09-16 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 26dc55c0-32b0-35ac-9156-f0b9c93df3e5 | -7.676 | -44.4879 | 2025-09-16 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c8359a18-fe08-38eb-9c2b-04c7fc898343 | -8.0196 | -45.662 | 2025-09-16 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 330.9 |
| a9b0cbe9-59fa-375e-b7e2-4a4ed02e5920 | -9.152 | -46.9812 | 2025-09-16 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 48e9b9c4-24f1-315f-8c57-421f6ba36ef9 | -9.7445 | -47.8468 | 2025-09-16 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 39b98e32-3e8a-35da-be94-b7d0783cc54b | -7.2956 | -46.602 | 2025-09-16 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 25ff026f-9a78-3223-9c62-a53e1f55d683 | -12.1861 | -44.0958 | 2025-09-16 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7458f9a3-c5d3-33c4-a707-a20f3b6214b5 | -12.7098 | -48.0094 | 2025-09-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 874102e6-26fb-3e73-a51e-708cf44a1470 | -8.001 | -45.6412 | 2025-09-16 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b1385150-1787-3d8b-a48f-ed4752bb2c72 | -12.6352 | -45.7652 | 2025-09-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 206.1 |
| be086094-5484-3dba-a245-7606440cb37b | -6.3372 | -43.1492 | 2025-09-16 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 892555af-4247-34f4-acfb-85e493c68938 | -7.9822 | -45.643 | 2025-09-16 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e4abd4a5-8442-366a-839c-e66eaf645b0f | -6.3558 | -43.1711 | 2025-09-16 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 9a55750d-2df4-3b22-8507-55db6ea88e8b | -10.802 | -50.6965 | 2025-09-16 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bdad67ac-e045-35fe-8bd6-864e02515894 | -8.9539 | -46.265 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| bab3bf9b-e6cf-3398-820d-e1457d3ac375 | -11.467 | -43.5485 | 2025-09-16 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README94.md)
