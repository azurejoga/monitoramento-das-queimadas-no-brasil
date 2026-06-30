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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68da3253-f886-3a21-9132-61ce6a089fa2 | -9.0228 | -59.5485 | 2026-06-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c718c8c8-c296-3478-80d1-00ad66becc66 | -13.2452 | -56.7965 | 2026-06-30 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 3ab2e940-decb-35aa-a3dd-c10300f960ad | -10.7777 | -54.0983 | 2026-06-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 40a5dbca-e2f2-3e7a-8d29-f5e6e5845498 | -11.6286 | -59.0169 | 2026-06-30 14:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f7fe508f-05ee-3022-9cdb-3df85faa5dc1 | -11.9113 | -43.3843 | 2026-06-30 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 83d4b9eb-12e0-3d3e-8b00-a40a07320cdf | -11.91 | -57.3735 | 2026-06-30 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 88c05877-bdc7-3140-8dbe-8f6904daae3b | -15.29 | -57.3823 | 2026-06-30 14:40:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5b90d1b8-9261-3585-91c2-3ad720b4bdaf | -11.891 | -57.3751 | 2026-06-30 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c7c597c6-4231-39da-91b1-c5bbb4057629 | -9.0229 | -59.5291 | 2026-06-30 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cd7d6ab9-9038-327c-af12-7004be39d76c | -13.264 | -56.8149 | 2026-06-30 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 211.9 |
| ae55afa8-1074-3395-864d-794f520d403a | -15.29 | -57.3823 | 2026-06-30 14:50:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8e6143e3-24c5-38aa-9b3c-63f8a3012f61 | -13.2643 | -56.7947 | 2026-06-30 14:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 667.8 |
| e2a4fccd-1f1d-39cf-9615-356d514ba90f | -10.3443 | -46.9142 | 2026-06-30 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 3d71a4d2-fd81-376b-8162-aa7be3c53aa7 | -8.9985 | -45.7418 | 2026-06-30 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c3abacd9-a69f-3680-ad23-0051adad652b | -11.891 | -57.3751 | 2026-06-30 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| df51eb6c-d49c-3365-8b9b-3ff97f0e3600 | -8.9619 | -45.6552 | 2026-06-30 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| d9ef2aba-1cb4-3fc8-a780-e8eaf964e4e7 | -8.9989 | -45.7191 | 2026-06-30 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c0397b3e-008d-34c1-9b9e-6e10d2cab064 | -9.1647 | -58.0595 | 2026-06-30 14:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 951270ce-b8a5-3605-8dfa-6cd09cdfb661 | -9.079 | -59.4874 | 2026-06-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| b93c3a0d-f513-37b4-9096-c6b6ec37a092 | -9.0228 | -59.5485 | 2026-06-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 32f15c49-0201-3e8e-a2bb-cee40dcf755e | -9.0229 | -59.5291 | 2026-06-30 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 33f3c3a8-151f-3bf6-8b9b-027ee77cbc44 | -11.9441 | -57.7091 | 2026-06-30 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 22f19302-84ef-346b-9751-3303b59d438c | -13.264 | -56.8149 | 2026-06-30 14:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 335.7 |
| 342e3c79-7194-38ba-abc6-e1f238d0bc6b | -11.6286 | -59.0169 | 2026-06-30 14:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3840c521-ee70-3222-845e-6ef1f07c7cfa | -11.9108 | -43.4081 | 2026-06-30 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 3296417f-b295-3578-be86-0ce298ef1f0b | -13.2452 | -56.7965 | 2026-06-30 14:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 6335e603-d2ac-3d8f-9f7f-8f851ef2d953 | -11.9097 | -57.3935 | 2026-06-30 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 4ef634b6-5cbc-3a20-b088-a8f98694a031 | -11.91 | -57.3735 | 2026-06-30 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 189.2 |
| f5191635-2d2e-32f6-b197-9ca2b04ed3a2 | -10.7777 | -54.0983 | 2026-06-30 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 6f585c0f-f4fd-32ee-8d14-6d08530c53bf | -17.712 | -46.7798 | 2026-06-30 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 1c62a017-bc73-3366-a4ad-97ea4f78596c | -11.9305 | -43.3812 | 2026-06-30 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 8407e190-7432-34c8-bc11-62ec76d9cc36 | -8.9989 | -45.7191 | 2026-06-30 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 22210d44-5f28-378e-9715-ea96632c4798 | -8.9619 | -45.6552 | 2026-06-30 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 47eba15c-710a-3884-9534-3638789a5629 | -11.6286 | -59.0169 | 2026-06-30 15:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| f2bbb5c1-4416-391f-bdb6-b52118831fac | -10.7777 | -54.0983 | 2026-06-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 97785990-0ace-3da7-9dd7-97d991f347f2 | -17.7114 | -46.8031 | 2026-06-30 15:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4da5995c-a89e-354b-b6b6-2530cdac3883 | -13.264 | -56.8149 | 2026-06-30 15:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 362.2 |
| 1db841ed-6381-36c2-8c2c-ac90ac3d32e1 | -9.0228 | -59.5485 | 2026-06-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8f6b49ae-341e-3461-bb19-f939a4cd1ea8 | -11.9097 | -57.3935 | 2026-06-30 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 91da2b33-7756-3d1b-8f45-8e5909b58254 | -13.2643 | -56.7947 | 2026-06-30 15:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 802.4 |
| 9389435f-c530-3426-a481-927d6f8941a4 | -9.0229 | -59.5291 | 2026-06-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 69f24b72-b5c6-3e27-afc8-69db9163bfa2 | -10.7774 | -54.1188 | 2026-06-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6517193c-40c4-3854-a28e-367eeb697c49 | -11.891 | -57.3751 | 2026-06-30 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| fd185585-6098-3623-bee7-099efdd0e70a | -9.079 | -59.4874 | 2026-06-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| daba8847-be04-3eab-98a6-cee2fd6d2495 | -17.712 | -46.7798 | 2026-06-30 15:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 153.5 |
| e446e3da-3329-3067-96f2-b2f0b560ff3d | -11.91 | -57.3735 | 2026-06-30 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 29b364f0-8770-3972-8a0f-8110bebc5dcd | -8.0928 | -50.9221 | 2026-06-30 15:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 27b64938-3838-3506-a0f1-e7ddbc2839bd | -10.3443 | -46.9142 | 2026-06-30 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 845e33e2-d253-332c-b761-37e5029aea87 | -13.2452 | -56.7965 | 2026-06-30 15:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 222.6 |
| afda782e-22ee-33a3-b569-8595a6ea6540 | -9.1647 | -58.0595 | 2026-06-30 15:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fd797de1-3f4c-3882-9d5b-19a18b8d32a6 | -10.3443 | -46.9142 | 2026-06-30 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 96bc8c96-bd9f-39be-bbda-590741b4d11b | -11.9097 | -57.3935 | 2026-06-30 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 169.0 |
| ff10cfb4-5629-3cf8-be8c-128083f0c217 | -17.712 | -46.7798 | 2026-06-30 15:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 174.4 |
| e008aa29-0df8-3d72-a6d2-4bea271b423c | -13.2452 | -56.7965 | 2026-06-30 15:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| bdaf8458-0dee-3407-9e2d-772506739177 | -13.2643 | -56.7947 | 2026-06-30 15:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 867.1 |
| 77a92661-533c-39db-8c0e-b3209993312f | -12.4281 | -58.4246 | 2026-06-30 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 636.0 |
| baa624cc-c128-327f-a2a8-696448b98ce4 | -11.6286 | -59.0169 | 2026-06-30 15:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e98b4c8b-87b2-3557-ba08-c678a1147487 | -11.9305 | -43.3812 | 2026-06-30 15:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f20f48d8-46a8-3b93-8c3d-fd9d9db568e5 | -7.7347 | -45.9145 | 2026-06-30 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 41e7af53-c34c-3aac-b331-2555b2cd7743 | -12.4283 | -58.4048 | 2026-06-30 15:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1289.6 |
| 51214cd9-4580-3b3a-8070-b3e1e9e11930 | -9.1647 | -58.0595 | 2026-06-30 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2c3f247f-e984-3d30-b179-2dbce617da11 | -8.0928 | -50.9221 | 2026-06-30 15:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 4faf0b2c-e370-3958-9173-539547306964 | -11.91 | -57.3735 | 2026-06-30 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 202.8 |
| cc481122-31e8-367f-b4fe-e3b2ab7e4bf4 | -9.0229 | -59.5291 | 2026-06-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| fd852c99-d9c0-35d4-b445-fa0f6cc353d8 | -11.891 | -57.3751 | 2026-06-30 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4e13dfff-13db-32d8-a072-765bedd03ca6 | -13.264 | -56.8149 | 2026-06-30 15:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 396.3 |
| 70c0b4a6-1f78-3f1e-9c66-60e76e8c093e | -10.7777 | -54.0983 | 2026-06-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4cdf0a4f-1893-3186-be76-5ae086279f48 | -8.9989 | -45.7191 | 2026-06-30 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 44381f7e-863a-396d-8f1c-f0ab8e69b0da | -10.7774 | -54.1188 | 2026-06-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4d32cd42-99db-314d-87b7-c7b1f43cd82a | -9.0228 | -59.5485 | 2026-06-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f819e723-8d70-315c-9e85-8ea8dde7be04 | -9.079 | -59.4874 | 2026-06-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 204.8 |
| ff4b855c-e2c4-37f1-81bc-25344912e3a9 | -8.9619 | -45.6552 | 2026-06-30 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d268cdfd-25bb-3a6f-8dbb-2fd948bf0610 | -17.7114 | -46.8031 | 2026-06-30 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 1e0f3eb8-b980-3b94-ba61-b034965aab0c | -7.7347 | -45.9145 | 2026-06-30 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 09dc0cfe-f58b-3c45-a890-348f60c80e66 | -11.91 | -57.3735 | 2026-06-30 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 09247a19-4f2d-3327-ae77-91d8aaa86464 | -13.2643 | -56.7947 | 2026-06-30 15:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 615.7 |
| dd75ef0b-92ec-3e65-b2e1-7d6f2a671b18 | -11.9305 | -43.3812 | 2026-06-30 15:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| c719a961-19c4-32e5-a740-c8c4dc9956bd | -10.7774 | -54.1188 | 2026-06-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2c429035-c349-3b0c-a300-3126bd2c7f39 | -13.2441 | -51.5655 | 2026-06-30 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 432a5135-ed07-31d2-9949-bae2cc7eb31f | -9.1833 | -58.0584 | 2026-06-30 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| e559fb65-23e6-3d29-8edc-fdb3fdf7d885 | -9.1647 | -58.0595 | 2026-06-30 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c66952c7-12a6-391b-b3f8-062c1f55bc8a | -9.0228 | -59.5485 | 2026-06-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| bdb579ae-4366-3380-92cd-654d195b2e23 | -9.0229 | -59.5291 | 2026-06-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 797c66b7-fff3-3099-932c-4f1b9f71fd37 | -8.0926 | -50.9431 | 2026-06-30 15:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d60c32f9-5a36-3e28-aea2-041813c50baf | -8.9989 | -45.7191 | 2026-06-30 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 86f2efec-8623-3f81-a9bb-85d9de5f86d1 | -9.079 | -59.4874 | 2026-06-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 200.4 |
| e85c3244-1505-3ca0-b478-982401b02e78 | -13.264 | -56.8149 | 2026-06-30 15:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 283.7 |
| a402f446-e3e8-31f8-b7bc-4aeb2435f711 | -11.9097 | -57.3935 | 2026-06-30 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 151.8 |
| cc4b5ae8-c05e-38c3-8d20-40b8bd0e505c | -7.7158 | -45.9163 | 2026-06-30 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| d93fc733-8333-3a3a-81e0-a8998e4063c8 | -11.6286 | -59.0169 | 2026-06-30 15:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ea62cef0-f564-3403-bad6-6c5cdff2e5f8 | -17.712 | -46.7798 | 2026-06-30 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 222.5 |
| a68f1ab1-2c7e-34de-a204-466b8bba15c1 | -8.1113 | -50.9417 | 2026-06-30 15:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2e36e50f-fcf2-37b0-a33e-3e71939f55f7 | -17.692 | -46.784 | 2026-06-30 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| bae1f468-8727-388d-990a-9e3334f74267 | -11.891 | -57.3751 | 2026-06-30 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 5d96fe3a-4774-3b2e-9a43-ecd2ac090f60 | -13.2452 | -56.7965 | 2026-06-30 15:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 53ef2a84-3159-3483-a3af-c64afd131f63 | -8.0928 | -50.9221 | 2026-06-30 15:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| af87ac2f-24af-3f87-a342-6726f6625dc3 | -11.6286 | -59.0169 | 2026-06-30 15:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 42a2bfe3-8006-3384-86ee-5a317e5b3f83 | -9.1647 | -58.0595 | 2026-06-30 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7a3962d3-e4b0-3364-a94e-20c5cd8161fb | -12.4281 | -58.4246 | 2026-06-30 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 340.6 |
| 6ada9bc0-96bb-3367-86dd-d20ad6e56664 | -12.4283 | -58.4048 | 2026-06-30 15:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 720.6 |


[Clique aqui para ver as próximas entradas](README23.md)
