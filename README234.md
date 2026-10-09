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

## Dados Diários - Página 234

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a45d7be4-46c4-31db-9548-f3a5fb6e11d8 | -10.4901 | -47.3201 | 2026-10-09 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a4d04d8b-97c4-3d5f-9afa-bd17d71db908 | -8.9964 | -45.9002 | 2026-10-09 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c742d534-6b3f-3218-9386-226542352313 | -8.9775 | -45.9023 | 2026-10-09 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7288b5ec-8945-3b14-a666-1d984cc00396 | -11.0566 | -44.0327 | 2026-10-09 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c84ff659-34da-359a-b051-6bcf14be6d35 | -13.1636 | -54.3591 | 2026-10-09 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| d111a0f9-f045-346c-a0f1-d1d40fe40b44 | -16.1334 | -43.4009 | 2026-10-09 12:10:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0b43d071-c14f-3591-bf99-dc7ecf8dd29e | -12.2346 | -57.1071 | 2026-10-09 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| bff1876a-a0d6-3fd1-980a-c6466af97bca | -11.4173 | -47.5833 | 2026-10-09 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ca0df615-11c9-39c5-9e1d-75486aa2dbd9 | -11.1242 | -45.6865 | 2026-10-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 06a4411b-d56d-35ca-af2e-8db8b7a916ac | -11.8302 | -43.6103 | 2026-10-09 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4607af70-42bc-38a8-8874-c09406df3c2e | -10.3161 | -46.2668 | 2026-10-09 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 6c73c672-e9ae-392f-a2bf-0b8720a1e481 | -11.8307 | -43.5866 | 2026-10-09 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 1b14348e-a6de-38a2-9769-417f3cfaf1dd | -11.2475 | -46.3058 | 2026-10-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 6e58abb7-1a75-3a77-9f8a-f46aaa975238 | -11.4128 | -46.6897 | 2026-10-09 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 454eb74a-580b-3e9e-87b1-49dac2061c38 | -11.2263 | -45.2834 | 2026-10-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 4759f2b2-3ed4-37b0-ad3d-42ef37a38b86 | -13.1824 | -54.3778 | 2026-10-09 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2d1bb7c5-d53e-31f9-b672-94834961e354 | -11.2259 | -45.3064 | 2026-10-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 1ea6d0ce-7f96-3eed-8a49-24e0802ca784 | -13.1827 | -54.3571 | 2026-10-09 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| a99642c6-07bc-37b9-8b35-ce3930eb0101 | -11.1051 | -45.689 | 2026-10-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 0befb78b-6da2-3e41-9a3f-2f2bcd063f10 | -9.3101 | -46.4509 | 2026-10-09 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 268f4c26-3068-33dd-bef3-0b0d5ed8e0c8 | -11.4131 | -46.6671 | 2026-10-09 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 9e0e651f-6ff4-3475-bdd2-f2aa671acd62 | -17.2322 | -47.7273 | 2026-10-09 12:10:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b2f29ca4-432a-3c57-bb78-cc39c8f28353 | -9.0147 | -45.9434 | 2026-10-09 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 3e6c1d95-bd2f-3c2b-b7ed-04ce44e164f4 | -11.0562 | -44.0561 | 2026-10-09 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 048c4712-578d-33b2-b497-a37a6fca2fb3 | -12.2348 | -57.0871 | 2026-10-09 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 51e2dfba-b9f3-337f-99e0-61a253abac67 | -11.5797 | -43.6728 | 2026-10-09 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 50197b42-fea1-32b7-b840-a86d6e91e035 | -11.5801 | -43.6492 | 2026-10-09 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 6cb2b45b-168b-3490-8f4e-f856ffda17e9 | -10.8983 | -45.5114 | 2026-10-09 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| be5da282-0e43-303b-abef-74b7fd72f894 | -13.1639 | -54.3385 | 2026-10-09 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 77f783b6-c69c-3cc8-b6f1-eab559c769b5 | -10.7475 | -46.6184 | 2026-10-09 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 448bd7a6-8c32-3294-9e68-84a9fda0532e | -8.9958 | -45.9454 | 2026-10-09 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 369d2c11-9282-3e2f-8f96-76876f62ceb6 | -11.6562 | -43.6846 | 2026-10-09 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3b709fee-ca22-3a01-878e-56352f82b44b | -10.8979 | -45.5343 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| ccb04fc8-9992-3790-b4cf-a6c3e25604d8 | -9.0826 | -45.1186 | 2026-10-09 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 9ebace57-6b0a-378f-a5b8-fcca2c1bcae5 | -13.1639 | -54.3385 | 2026-10-09 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 949f3288-f536-3aeb-a577-875e4cbd33d5 | -11.0562 | -44.0561 | 2026-10-09 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| e02475e4-faa8-382f-8293-70ca8dfb5123 | -9.1297 | -45.8179 | 2026-10-09 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 8276e4c3-46ac-356f-a035-b10ba8aaa723 | -12.0058 | -43.464 | 2026-10-09 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 776.5 |
| 863aa2d8-1f72-3d1d-baac-5c2f5012a2ec | -11.2259 | -45.3064 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 292.6 |
| e49187bc-4f79-305b-a76f-a53efad33383 | -8.9684 | -45.177 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 15bc7d8d-d236-3230-8e88-39e3301a0e34 | -12.2348 | -57.0871 | 2026-10-09 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 342e5e45-ea68-3bf4-878d-b739d5718cc8 | -11.1051 | -45.689 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 8c5bcf5d-d71d-3e0a-adc1-fc7167fc2deb | -13.267 | -46.9649 | 2026-10-09 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 4a154517-f46e-3b52-a535-b2a670aa59a1 | -11.8302 | -43.6103 | 2026-10-09 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 85ef1250-c179-3626-af0e-1d3e981ca1e0 | -8.9687 | -45.1542 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 158.3 |
| a3c15a17-6b1d-3803-9377-8131bcfdc7ab | -10.4901 | -47.3201 | 2026-10-09 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 99da0043-70c0-3b44-b666-090ea024d633 | -8.9494 | -45.1791 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 01622680-87df-3a8c-9125-3863da5da947 | -11.5993 | -43.6462 | 2026-10-09 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| f64ccbc4-2529-3d12-a5a5-8b51e87825bc | -13.1827 | -54.3571 | 2026-10-09 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 29ea8259-42d2-3a6c-b9cc-288fdac1755b | -11.4131 | -46.6671 | 2026-10-09 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 258.6 |
| 37555ee6-f7c4-3447-bdd3-420fab094c26 | -11.2475 | -46.3058 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| d363d0ed-5792-3b7a-852c-c34290a2ec6f | -11.5797 | -43.6728 | 2026-10-09 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 42147530-bff0-3070-a277-639b17f00737 | -13.1636 | -54.3591 | 2026-10-09 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 38f66d1c-9094-325f-b6e5-4f07a927a993 | -9.0147 | -45.9434 | 2026-10-09 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| b501b568-ad04-34bc-96e3-b2c50c120157 | -11.2263 | -45.2834 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 254.2 |
| 1cf0168c-f3c7-3d04-b37f-e76878108c19 | -10.7479 | -46.5959 | 2026-10-09 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 7dc6d1ea-e08c-3718-b1cb-925451db9270 | -13.1824 | -54.3778 | 2026-10-09 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b0e91b47-1098-3d79-952d-69c032552de9 | -10.3161 | -46.2668 | 2026-10-09 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| f71aaa45-36a7-38d7-b48b-1b36c11ed184 | -11.2849 | -45.2063 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 01863f83-7ea7-3c7d-af2c-351849d2a83a | -11.4173 | -47.5833 | 2026-10-09 12:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4312f1b7-c222-3f89-903e-a885b5af3190 | -8.9775 | -45.9023 | 2026-10-09 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a2e07c12-d8f5-37ca-8fbb-967c1079a4c5 | -8.911 | -45.229 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 06c29be2-3516-3bae-94f8-d03db6da4939 | -12.0054 | -43.4878 | 2026-10-09 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 400.7 |
| 8ab8d724-e0ab-32c0-b528-15f29ecad09e | -9.1012 | -45.1393 | 2026-10-09 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 359.4 |
| e4fdc953-7011-3a58-9990-fd74aaafcf27 | -11.4128 | -46.6897 | 2026-10-09 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 243.6 |
| dd266805-20d6-31d9-9e06-5f3732480ccf | -8.9107 | -45.2519 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e682629a-8e3c-30bb-8007-3da0dd24d1cc | -16.1334 | -43.4009 | 2026-10-09 12:20:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e5452a19-0eb7-3983-b229-dc78198051c0 | -11.0566 | -44.0327 | 2026-10-09 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| dad2c7db-511f-38b8-aef8-b039c81c0847 | -13.2015 | -54.3757 | 2026-10-09 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5c684134-140f-34d0-8bdc-f5d418702641 | -11.1242 | -45.6865 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 3a6be149-bd64-3fe9-b396-f900f469ccfd | -8.969 | -45.1313 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d31a4238-6f0c-3563-8447-55f544758156 | -11.5801 | -43.6492 | 2026-10-09 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 9c0acb52-8580-324b-a676-e32cb24a7f7a | -12.0063 | -43.4402 | 2026-10-09 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 206.6 |
| e896c9b6-3068-38cc-8592-ac60ff0ca24d | -8.9113 | -45.2062 | 2026-10-09 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 58079e3d-9b60-3c9e-912a-07f8d1ae51f2 | -9.1015 | -45.1164 | 2026-10-09 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 217.6 |
| b864d269-026f-3e3d-8806-6e6aa9b916e6 | -12.2346 | -57.1071 | 2026-10-09 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 29bc6cdd-91a5-3f67-ba82-cd0546763992 | -10.917 | -45.5317 | 2026-10-09 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| fc176d7d-8024-325f-995a-ac9c183f9234 | -11.8307 | -43.5866 | 2026-10-09 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 48bf47a1-57ac-36b0-b8c9-72fc2431a7a0 | -8.969 | -45.1313 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 248.5 |
| 7f66de23-c4f7-3bd8-90be-c7b818b7d4c8 | -9.8627 | -44.8656 | 2026-10-09 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| f6a0d650-ccbf-3431-b17d-7dd8a080b4de | -11.4131 | -46.6671 | 2026-10-09 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| a1fb8a66-fc22-3229-8a5f-b65de8d89fdf | -10.4334 | -47.3046 | 2026-10-09 12:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| cb4075b3-2a14-3573-90c2-9804bffddde1 | -9.3101 | -46.4509 | 2026-10-09 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 77040853-cae3-39ca-a6c7-3fa6c2775aaf | -11.2068 | -45.3091 | 2026-10-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 7e4a0b7e-e69d-3596-98d0-4b8a87c71e7b | -13.1824 | -54.3778 | 2026-10-09 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d200fe57-3924-34e7-89f8-39d65d65538c | -11.9865 | -43.4671 | 2026-10-09 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1451.4 |
| 1fd04311-42ef-32b8-ad03-2e07b72c0ad9 | -8.9964 | -45.9002 | 2026-10-09 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 270.0 |
| ced26845-e502-3d20-956d-f3a4e358e411 | -12.2348 | -57.0871 | 2026-10-09 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 07789592-56da-30c4-aaac-7923cf2090c8 | -11.5801 | -43.6492 | 2026-10-09 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5831d518-c79f-3e1c-94b8-e0726a86e329 | -8.9494 | -45.1791 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 417420db-c3d9-306a-99ab-e99d0069a362 | -10.9174 | -45.5088 | 2026-10-09 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 896824c7-d62b-3523-b2df-519c91ba6b0e | -11.0562 | -44.0561 | 2026-10-09 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 0582934b-57d2-3f53-a2e4-50ad61c87973 | -13.1636 | -54.3591 | 2026-10-09 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.1 |
| ae05d5ea-7d9b-3323-9293-5c99b2ec095c | -12.0054 | -43.4878 | 2026-10-09 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 317.8 |
| 499dd521-8d41-3aed-9600-d674bbc183b0 | -13.1827 | -54.3571 | 2026-10-09 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 7f6faa60-e6b2-3ac6-92df-cd6f2018c352 | -11.4128 | -46.6897 | 2026-10-09 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| a0e30cca-ceaf-3fab-9931-c413364ad9eb | -13.1639 | -54.3385 | 2026-10-09 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 51511a06-9d24-363f-8af2-6c1c24f5f5c6 | -9.0826 | -45.1186 | 2026-10-09 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 89541ce3-19e1-373d-8069-043362c7cecd | -8.9684 | -45.177 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 331529ca-6e67-3b46-bc4e-0b6f8c556d5e | -8.911 | -45.229 | 2026-10-09 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.6 |


[Clique aqui para ver as próximas entradas](README235.md)
