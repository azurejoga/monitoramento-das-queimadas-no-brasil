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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67160ed9-2254-376a-9cb4-42f1c38170c4 | -12.2215 | -44.2543 | 2026-05-20 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0a99391f-8bd8-36db-95b0-39e0269ac6cc | -12.6011 | -44.521 | 2026-05-20 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 52766ff6-dcc4-31fc-93c4-5656142e3fcb | -10.6467 | -42.3141 | 2026-05-20 13:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 620.4 |
| 23042089-0022-39b7-bf04-447a0b6aa53c | -12.2408 | -44.2512 | 2026-05-20 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f8d49d1b-f37d-37f7-9f2d-57fac4528b15 | -9.9688 | -52.4585 | 2026-05-20 13:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| ddad5ffa-b5b1-3d05-9426-a41eb9e64f24 | -10.6659 | -42.3112 | 2026-05-20 13:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 261.8 |
| 770d3cd2-6db8-32ed-b2a4-922e28e03f5a | -12.2215 | -44.2543 | 2026-05-20 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 15d4e957-c413-33f3-b036-fb58782257da | -12.6011 | -44.521 | 2026-05-20 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5997de1d-9999-3edb-a6e1-b662be353a48 | -14.9166 | -47.7376 | 2026-05-20 13:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0adbfa30-4839-3038-9bd0-0e23070bcd24 | -6.8185 | -43.8295 | 2026-05-20 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 850bb596-d4be-3a63-8f22-6d5d27ff8750 | -9.9688 | -52.4585 | 2026-05-20 13:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| d479ea30-1aae-372e-a70d-1d5c36c97d0a | -6.8185 | -43.8295 | 2026-05-20 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cdcf484e-fc8d-3590-93bd-8072f1e36f23 | -12.2408 | -44.2512 | 2026-05-20 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f5e69a7c-35a5-36d6-b4ec-82d948c1144c | -12.6011 | -44.521 | 2026-05-20 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 84fc0d47-bdd4-3b78-a57c-fa42a0596ead | -10.6659 | -42.3112 | 2026-05-20 13:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 245.6 |
| 4a285f51-4348-3033-82a6-abe42b056405 | -12.6011 | -44.521 | 2026-05-20 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| b2c2a5fc-0f41-3d8f-9b5d-906d5b8ca42c | -11.1108 | -46.5044 | 2026-05-20 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0d1c9da9-8345-3d6b-a899-d53388407e22 | -11.9741 | -47.3762 | 2026-05-20 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 26ddb020-853e-3d67-92b7-dbfa034706b5 | -9.9688 | -52.4585 | 2026-05-20 13:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| cd6090b6-3902-39a1-930d-9f3ad3674b2e | -6.8185 | -43.8295 | 2026-05-20 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e1730f06-16ac-32cc-b48a-2ed18b8a9cd5 | -10.6659 | -42.3112 | 2026-05-20 13:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 214.4 |
| d12d6e1a-6c2f-32c5-8af5-5289ff0dcd14 | -9.95 | -52.4602 | 2026-05-20 13:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bc1ac286-05ac-336d-bf01-09fbb8c46342 | -11.9744 | -47.3539 | 2026-05-20 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7f8fad2f-a60c-3fee-98f5-c654f92a5bea | -9.95 | -52.4602 | 2026-05-20 14:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9e798ca0-d930-37c6-9973-3430bbdb2dc5 | -9.9688 | -52.4585 | 2026-05-20 14:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9ca9aa51-e73a-3808-9970-4d9434d4c62a | -10.6659 | -42.3112 | 2026-05-20 14:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 215.6 |
| 2b29bc8d-dd95-3745-baff-431e807f7fe9 | -11.9741 | -47.3762 | 2026-05-20 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 97283706-9d66-3e30-9339-c41252462c78 | -12.6011 | -44.521 | 2026-05-20 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 72aeda97-cbf3-3ba6-8eec-31b21dd08747 | -6.8185 | -43.8295 | 2026-05-20 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 971afd33-7859-340e-bc0f-ec75048bf844 | -11.0918 | -46.5069 | 2026-05-20 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 190c4b7e-7081-3fd9-b36c-5d7cbf95ddd9 | -9.0018 | -46.9301 | 2026-05-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 003a1f74-949f-37a1-a06e-429e7954e34d | -10.6659 | -42.3112 | 2026-05-20 14:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 199.6 |
| e9af6251-e9e1-3ac6-a5f7-a3031d8e9ab7 | -11.9741 | -47.3762 | 2026-05-20 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 17182e31-921d-3e83-a9ac-5b16e83df918 | -10.8548 | -49.6199 | 2026-05-20 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 550727c5-2e21-30f0-b2b8-d9fdb7aab0ae | -11.9744 | -47.3539 | 2026-05-20 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c35dc61f-6ece-3720-9c97-87567d4cf761 | -9.95 | -52.4602 | 2026-05-20 14:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 347466fb-c367-3abb-9d2c-bd463f648765 | -9.9688 | -52.4585 | 2026-05-20 14:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 001a121a-daa7-3f65-980f-31ab55b0f86c | -12.6011 | -44.521 | 2026-05-20 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| cbb01b24-ff61-305b-b2a0-fa010b704245 | -12.6011 | -44.521 | 2026-05-20 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 9a1e23bd-312e-3d4d-9549-35e77f081dd4 | -10.6659 | -42.3112 | 2026-05-20 14:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 233.0 |
| c40c44be-1935-35e1-beff-086fb8da0589 | -11.9741 | -47.3762 | 2026-05-20 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2303e4ed-3fcb-3336-a538-7433bd8ecfcf | -9.9688 | -52.4585 | 2026-05-20 14:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 828ffe28-fe94-3a19-8f79-e415aae838f3 | -9.9688 | -52.4585 | 2026-05-20 14:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 03b1ad69-511f-37aa-a17f-9f759d30450e | -11.0918 | -46.5069 | 2026-05-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e595ad58-b7f7-386f-be1d-77327b8a4206 | -12.6011 | -44.521 | 2026-05-20 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 6de6239a-cfd1-3bbe-a516-e10e3b4876ea | -10.5759 | -46.6622 | 2026-05-20 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 87121e99-c1d4-3965-8b3c-44f739339140 | -9.95 | -52.4602 | 2026-05-20 14:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| aaf915e0-7a3e-3457-bcbc-48d9bd330b3f | -10.6659 | -42.3112 | 2026-05-20 14:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 200.6 |
| f9beea43-4e8c-3aab-b0be-da78c6e55228 | -11.9741 | -47.3762 | 2026-05-20 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 451d5349-f21b-3bfe-b47e-0f16acf088d1 | -10.6467 | -42.3141 | 2026-05-20 14:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 413.3 |
| f27e987f-b413-3796-9e25-135be2454289 | -9.95 | -52.4602 | 2026-05-20 14:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 62440b0b-2b2e-3350-a7dd-b05f6edcbbd4 | -10.6659 | -42.3112 | 2026-05-20 14:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 144.9 |
| b3ac4bc2-a963-3a56-8bea-7b9c9961000b | -11.9741 | -47.3762 | 2026-05-20 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5e69064f-2325-341a-bd4d-9d93980bbe76 | -12.6011 | -44.521 | 2026-05-20 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7fc8cd12-595a-3889-ae54-2442339f2d80 | -10.5762 | -46.6398 | 2026-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d1ba7d93-8754-3d04-b225-edf156312937 | -10.5759 | -46.6622 | 2026-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 69af0bfd-71b3-3bbb-9de9-c386fd027a13 | -9.9688 | -52.4585 | 2026-05-20 14:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 849edbc4-9466-36d4-a210-c269fba6c7e0 | -11.0918 | -46.5069 | 2026-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| bb2cb7fe-3d1b-3876-bf95-68a2ba461795 | -10.5949 | -46.6599 | 2026-05-20 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| dd3b7604-5802-3dbf-bb50-54d896ffc963 | -9.5204 | -46.2704 | 2026-05-20 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b41f0737-7b17-3445-b3cb-2fbe0cf1ef8b | -9.9688 | -52.4585 | 2026-05-20 14:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a48a3eba-8f0b-3681-acae-e423192232e1 | -12.6011 | -44.521 | 2026-05-20 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| fae30a08-2bd4-39e7-ba75-8808cef1046a | -10.6659 | -42.3112 | 2026-05-20 14:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 183.3 |
| e3ab6f62-1497-3c91-b8bf-258f95cf3c93 | -9.5204 | -46.2704 | 2026-05-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f4bbc92f-4ba1-3d99-b256-b27de256b1bf | -11.1101 | -46.5495 | 2026-05-20 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 40032c7e-108c-3ba1-983d-67b56da4331b | -10.6659 | -42.3112 | 2026-05-20 15:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 167.7 |
| cce4d31f-6335-38ff-81fd-dc772d9313db | -11.1108 | -46.5044 | 2026-05-20 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8cc7f61a-83c4-305c-8668-2dfa6a8f6dcf | -11.1105 | -46.5269 | 2026-05-20 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 68f74f6e-d242-3083-8e8e-e4d8ccebf4e4 | -12.6011 | -44.521 | 2026-05-20 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 324bbf97-11e2-3263-8601-e0b4381a5df8 | -11.0918 | -46.5069 | 2026-05-20 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 28316d1f-62d2-3efd-8f71-510765233ff9 | -11.1101 | -46.5495 | 2026-05-20 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ad8247a6-79cd-393b-ad48-01adc16b4d4e | -11.0918 | -46.5069 | 2026-05-20 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 311b3ab7-4b11-3ad8-a7dc-f6ccc77a8e12 | -12.6011 | -44.521 | 2026-05-20 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| dc65a15d-1406-3c26-84d3-84f00064a87e | -11.1108 | -46.5044 | 2026-05-20 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 72238d1e-f9ec-325f-bd9e-1825b7644566 | -10.6659 | -42.3112 | 2026-05-20 15:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 176.8 |
| 4af09740-54be-3b67-bcd6-cc94eebc4ce7 | -12.6011 | -44.521 | 2026-05-20 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6bdf3017-65b0-3366-8393-8268ace0d0b6 | -11.1108 | -46.5044 | 2026-05-20 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 2f5e1b09-cb25-3150-bbcf-276786998f79 | -10.6659 | -42.3112 | 2026-05-20 15:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 29a99746-bb0a-3033-9b58-e697a404855e | -11.0918 | -46.5069 | 2026-05-20 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 028a0292-eae8-34b0-9b3d-858a85d8defc | -10.6659 | -42.3112 | 2026-05-20 15:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 130.5 |
| dd259c17-45db-387c-940a-7bfb13139607 | -11.0918 | -46.5069 | 2026-05-20 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8190900c-183a-36e7-b36f-ba2510590ec2 | -11.1108 | -46.5044 | 2026-05-20 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fb37b13e-3cdb-361a-acd1-ba42be245742 | -10.6659 | -42.3112 | 2026-05-20 15:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 126.3 |
| f5ffc41c-8181-39f4-8c25-774cc180a42c | -11.2743 | -49.4642 | 2026-05-20 15:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e15dcc12-3ea7-3c8e-83d8-47c849653b6d | -10.6659 | -42.3112 | 2026-05-20 15:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 137.2 |
| fa43eeab-dde0-39ad-9fc0-643b4ebae673 | -11.2743 | -49.4642 | 2026-05-20 15:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| cfe1102e-374b-3a3f-9bf1-d8391c52cf2e | -11.2743 | -49.4642 | 2026-05-20 16:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| eeea4527-5a38-31d2-8941-165989162940 | -10.6659 | -42.3112 | 2026-05-20 16:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 745ffe30-434c-370a-93fa-c63184f6b3e9 | -12.1309 | -53.3093 | 2026-05-20 16:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e6bf7428-f5a1-3a36-bf5e-2ae2d9749d09 | -11.2743 | -49.4642 | 2026-05-20 16:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8b90e4a2-8c5d-3017-b88a-87c150a3969b | -10.908 | -49.8724 | 2026-05-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f4818b05-c23b-31cf-b026-b8ad30bc6e66 | -10.889 | -49.8745 | 2026-05-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 088a709c-ec26-359f-9ee0-15f4274cde53 | -11.2746 | -49.4426 | 2026-05-20 16:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f1ca0b38-4130-38e6-b7f7-0ed56ace4e5e | -10.889 | -49.8745 | 2026-05-20 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |


