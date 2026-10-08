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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 948f9b5f-6257-357b-aa88-ff6b56460284 | -2.99534 | -54.14283 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67c50391-c405-30ae-b7b1-ccd572152c64 | -3.47096 | -49.93609 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3509410a-38e2-3fce-9b91-7c4c59e80b8d | -3.54078 | -50.09943 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61cb97a8-9c05-3d4e-9887-6c5f6c0cce68 | -6.99567 | -59.11216 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77d47ae0-bd1b-38ed-8a9f-a147c9da6ab5 | -6.85475 | -55.78347 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f3fcea-d712-35b0-900b-cc4a32322d10 | -2.50648 | -56.13836 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0bcc9fa-b055-31ce-a1a8-61cd1a0bf59d | -4.06272 | -59.84114 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb3355db-8fae-3f71-bfab-a98c9d765ed3 | -3.02216 | -53.95099 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0567ee6c-491f-3e8b-8621-a0e1a58ec4f3 | -4.53777 | -54.98782 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1cf5855-7134-38bb-86a3-9c53eaadcb15 | -2.72513 | -57.4632 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08242b51-294d-3ec9-98af-ad8ce3ed3430 | -2.97294 | -54.11696 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdbba8b6-4523-3e41-9271-f2416f8a72f1 | -8.732 | -45.15618 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0ab97bfe-226d-3cf7-9e47-86e8bd2dcdd1 | -3.00013 | -54.18439 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbaef227-a60a-3659-883e-8decabe05d92 | -7.60569 | -42.38023 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f65952bb-faaf-33c6-ac4e-d08df2a4f151 | -2.38539 | -56.13622 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a86eb0d6-21f8-3012-972f-00c80f29126b | -2.96144 | -54.16476 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1da312e6-af96-36cc-93c9-2f4e8acad709 | -3.30444 | -54.06178 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a139bb04-f6cf-3aff-a482-699ae5dfcffb | -3.10822 | -53.76733 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82fa28cd-6974-3b10-bbf2-5260d3b1a056 | -3.5362 | -54.67091 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2767fe35-0f43-306a-b89d-c730b5b09633 | -4.31151 | -50.78645 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd233e53-696c-3a86-8bf8-e7a2ea8e8b9a | -5.97676 | -55.38362 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d2e619b-eb62-3897-a6e1-4b17aaf2f83a | -6.95467 | -45.26164 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d903d200-1620-31c2-bacf-0bd6eeeda18b | -4.26871 | -54.87233 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49a9d6ea-ac9b-306f-bd13-e2862dc7a716 | -2.84117 | -54.07112 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57346729-4927-3a5c-bac9-4ea18545ca0d | -3.51725 | -54.66793 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0043f12c-1735-3864-9abe-c93f89b20936 | -4.9254 | -55.86051 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2e59613-7526-3ab6-9b42-f49a3a893173 | -3.10168 | -54.98746 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1730a773-f8a7-3a52-809c-376bdcde1639 | -5.24266 | -50.90501 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3be0f72f-3f5e-328d-911c-01f365eba681 | -3.10764 | -54.16778 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ef5426a-404b-3640-8e11-a72a6d7e2a0d | -5.73244 | -45.16221 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6dd79b87-9bff-35da-bff7-342c578d4a2c | -4.74911 | -55.65675 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06838f00-eb89-3388-912e-f7ec05ffe3af | -8.72753 | -45.15556 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0ffb4bb4-7ae4-3701-a27e-55a56943933b | -3.1005 | -54.28466 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c238db52-30a6-38bb-a6f0-b0e07046b3ba | -2.98052 | -54.14061 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a91ff37f-1e22-3bd7-b75d-f45047952222 | -3.29743 | -54.01218 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee4bc10f-9b9e-3ec6-8195-468b1a68eaae | -2.99914 | -54.23862 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b5a2b8b-c050-3159-abcf-f68588724222 | -5.4939 | -42.85516 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ee8b0ef6-7155-3ec5-be34-f6ed9f3a1478 | -3.53855 | -50.09204 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08dc5da5-9cec-3ef4-aead-a8cc09922e81 | -2.49398 | -56.1079 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80c5ee1b-532e-3f7f-86b6-7ded982d3b63 | -3.43467 | -59.53859 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da14900d-29fe-3130-9820-21eea90a528f | -3.87539 | -55.82045 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f48d018-7d8d-3d4f-8188-e262ba08db2f | -3.35328 | -50.47415 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fe337e2-7ca3-3fd9-8f35-8091c1604f72 | -4.56589 | -54.95605 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 470c2aed-7a0b-30a4-badc-4d15c21927fb | -11.10035 | -44.00389 | 2026-10-08 04:46:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6851d00a-18d7-3a31-8346-eb2523190323 | -3.33108 | -58.16573 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9e45383-ad7a-35c7-8e33-d219c7fd574f | -4.34729 | -55.13046 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94d59e40-3582-3d14-8b70-2d8c1782f1a5 | -5.72585 | -45.15482 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7bab29bf-39f7-3199-885a-014843dec01d | -7.14734 | -46.52051 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a4d5ab9-dc20-39c2-880e-52b8b2c164b5 | -3.01801 | -54.19152 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a56fd4e-cc0a-32b5-a1d1-f90d97949813 | -5.1758 | -45.33903 | 2026-10-08 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bc10114-8d92-3929-bab0-3fea6885318b | -3.74106 | -55.95054 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aac1f54-8289-35f4-9f36-c17872299b6c | -4.92083 | -55.86338 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae6bbaa3-eee4-3792-8557-ec5fcc4708ff | -8.05846 | -55.29539 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a3dba88-84d8-3b47-bd63-c695b721c332 | -3.29831 | -54.02995 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30f83753-a63d-3ef1-b9eb-5cfde95866ff | -2.56869 | -56.15599 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0661c2e0-a06e-3f41-9606-2f73c1f60d2d | -2.57951 | -56.16972 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f7de5b1-f62f-399c-bbe1-3938a10b2f0c | -4.88121 | -49.10838 | 2026-10-08 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2eb9e34-7d4b-3119-8aab-419651a7dbfc | -3.03588 | -53.93548 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccb18178-a6fe-3fa1-99f5-64d97ef15a9f | -7.38441 | -46.23989 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5ee7825-521c-3bff-9da9-0f16fc745d8b | -4.97812 | -50.57108 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b867310e-5462-3825-b5ff-11db5b38010c | -4.88185 | -55.85065 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e74685a7-76b1-3df8-ad87-2fa6bca05da4 | -6.23912 | -52.67894 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3a0b26d-c3c5-328b-9bb7-0adb60d045ae | -8.59145 | -44.85824 | 2026-10-08 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa312f60-9886-37fb-aecc-fd602302b481 | -3.30637 | -53.86517 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ffa390a1-2955-3d20-827c-ac476041f947 | -4.06481 | -59.83753 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16658257-b48b-3548-9084-f17b8c72b830 | -3.98277 | -56.2149 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08315bfa-65fe-3b8a-84bb-98fe85f418fa | -3.26345 | -54.67707 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 51558045-7ecc-3b96-b782-e362798714ef | -8.73709 | -45.15236 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 44b978b7-0b83-3360-927a-7a9affdf1e8e | -2.78689 | -54.08595 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 492847b0-35eb-3b37-ba66-5299d62dd7cd | -11.86176 | -43.55988 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a132c4-354b-3503-93bb-93018336a21e | -5.76938 | -42.05012 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eabfed5d-af87-30f9-941e-db51f2eac131 | -2.90263 | -54.01807 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e5fb0a-f77b-3369-87ba-86fa45bb5b0e | -3.83612 | -55.9814 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 278fdc45-b3a2-367c-857e-7258a43db6e5 | -3.28835 | -54.06818 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08b7dd7-3261-369e-b123-b1474c533ed6 | -9.30976 | -46.44788 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a501fb25-c8c8-3be0-9e54-000c3c23e69b | -3.08026 | -54.26785 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f007f7a-b34e-34e9-bfb8-753cbff61bed | -2.49873 | -56.13263 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b381736-5efe-3ab7-a2c3-39142b009504 | -3.00025 | -54.11206 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c23ff356-59d2-3cab-9f1f-98111f5bde5f | -8.90243 | -49.97518 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c68e9dca-dd20-392a-b4d6-bc2963dda59d | -4.08096 | -55.38127 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d94ddb1-7f05-3e28-bd91-203c2964f6c9 | -6.31891 | -43.34894 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 117dd3b3-1ec6-3325-a904-634553862b55 | -3.48011 | -59.46072 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50abb6f5-eab7-3c75-bcf2-896a24bb9d06 | -7.07699 | -40.94102 | 2026-10-08 04:46:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f14454a8-233a-3a5b-867a-2d6f040335c0 | -7.1874 | -52.6282 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 175d7c41-962a-3a51-9c6d-490a303ae56c | -3.00588 | -54.24426 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2f564b4-37f3-3fc8-8aaf-e96ea057da79 | -3.31865 | -58.27197 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b8aef04-0684-310d-a9c6-87c86fd01792 | -3.03809 | -54.53143 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f3f5dde-d3d8-3d08-ad95-5d109d6035bc | -4.71493 | -47.44535 | 2026-10-08 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ce8e4a9-8255-3d20-bf38-5d8e91a2abc7 | -3.14966 | -54.09356 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcb5eaf9-482b-3a99-acbd-f63f3de4dd11 | -2.9441 | -54.10782 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d7e38cc-2fa4-3f4d-8867-815746eb6497 | -4.45343 | -47.92495 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8fbe7042-1a5c-3967-9637-8df1eca7e86e | -3.01364 | -54.12313 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| aa06646d-b377-3bff-80fa-7bec88878b6e | -10.49786 | -51.94103 | 2026-10-08 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe5396f1-7d16-394c-948f-8df6844fe06c | -3.7016 | -53.39713 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48e48ad2-ae1f-3e3a-b614-f41293e79036 | -5.29566 | -60.08636 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0107bfa-8986-3a09-801d-683829f5cb8a | -3.09606 | -54.28854 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7ff99c3-5dbb-3773-946d-2b0871e7801e | -3.51311 | -59.32978 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f514806b-b409-3a25-932a-e919f14c0c67 | -3.03175 | -54.23742 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5ab6601-62f1-3a62-82bb-6a8729ce2900 | -3.29673 | -54.01649 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4765ae90-e5a0-3269-a139-8718fd8ec2df | -11.63224 | -43.69946 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README98.md)
