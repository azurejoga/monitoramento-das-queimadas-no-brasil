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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1cc6e47-9f3b-39d9-aebe-b19522fca816 | -9.32683 | -45.48097 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 095b13da-1b16-3c7b-8101-ee937d47c883 | -8.94259 | -46.97529 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b78f9bdf-1550-33f3-be09-f4a4b380f6eb | -9.2113 | -47.90867 | 2026-06-17 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 175f3dbf-b968-331e-88b7-5d704fae1a4d | -12.17798 | -52.7885 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2a27c298-baa1-3b01-92a4-6df6f7d3b265 | -10.98295 | -47.74472 | 2026-06-17 04:00:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdffb513-ace0-3ec3-badd-bdd42d6f7f51 | -9.33836 | -45.48437 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ea65e15d-c1c4-3a84-99c6-750c9efd21b4 | -10.97399 | -46.44886 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd2738b-e9fb-3ef6-9961-472ddb978e1d | -11.88498 | -43.83032 | 2026-06-17 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6836e965-3651-3c82-bad1-fe55df2f4f1c | -13.57718 | -48.20488 | 2026-06-17 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 409f961f-196a-3a33-87a9-93cf97d190e4 | -9.31809 | -45.47372 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdc992ac-ddc1-3989-9547-c3947e8245d2 | -11.88615 | -43.82954 | 2026-06-17 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bac9a17-7e34-365c-8f4e-bd28a07795ba | -8.96752 | -46.96156 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b333106-b069-350d-92f4-d466dd4e7fda | -10.94884 | -39.28045 | 2026-06-17 04:00:00 | NPP-375D | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4cd4f4ac-57ef-3d71-a392-23b7de60d45c | -9.31994 | -45.47535 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c532567b-6763-3ab1-bb92-0ae936de0f14 | -9.33934 | -45.47901 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 5be0d12f-2a16-3393-b4a7-2bc123dbe3e2 | -12.84032 | -44.37226 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 196205e4-9776-38d9-b94a-b96426b9e27b | -12.26328 | -43.50115 | 2026-06-17 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f33d3b15-5cd2-3444-8764-80d4ff775ae6 | -12.17319 | -52.77806 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a0b2ce13-d99f-332b-a2fe-b6dfe338081e | -9.2124 | -47.90792 | 2026-06-17 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8c63231-cd4a-39cc-b540-dad960edef7f | -9.32479 | -45.47628 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d998e69b-4f54-3b34-8e73-17bc54e2460e | -10.93007 | -44.66872 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5576b8d7-7c90-39e3-8ae7-cf29fe18b211 | -10.40242 | -49.44695 | 2026-06-17 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e98f159f-81ed-345f-8521-e01b150dc061 | -9.31025 | -45.47345 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83e0745e-5885-3bab-aa7b-0f522bc386fa | -9.33654 | -45.48281 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| dba17218-f8cc-3598-88f6-9dee7516f224 | -9.34615 | -45.46924 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cc63fb9-788f-3da9-b313-00b8fa0b0b5c | -10.56204 | -46.23043 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7859864-dcf1-383d-bf7e-e80946777204 | -12.26669 | -43.50555 | 2026-06-17 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b72f86ee-602a-31e9-bf97-455b4c9e1683 | -8.97112 | -47.00214 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ba6a912-faa6-3dc5-b754-dabeda166717 | -13.57647 | -48.20844 | 2026-06-17 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46dd8839-d7b8-3deb-a45e-25673414accc | -12.18519 | -52.79011 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5ce4444b-b635-38b8-acd8-fd34a3fea2f4 | -12.00038 | -45.11866 | 2026-06-17 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d75aca8-ec89-353f-90d6-054a53f09a9c | -11.39412 | -47.81897 | 2026-06-17 04:00:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09325aeb-3a0d-3672-911e-e3d22da09263 | -10.55205 | -46.22848 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b231dbf-2370-37db-a059-bca75ae786fe | -12.44795 | -44.7502 | 2026-06-17 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f345ad-ce13-38f3-8882-8bc84952e31f | -12.17158 | -52.78537 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 115f9e1a-43c5-3050-9b7b-8c916566fd74 | -12.20681 | -52.79506 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d50e1c0-031e-32b8-9ba4-18d2d0d391f5 | -9.32778 | -45.4756 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 524e8925-5e8b-3169-8f64-c7952171a31d | -12.17948 | -52.81844 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ad2a737-56b4-3671-807e-e62dff72c86c | -12.17879 | -52.78697 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 601a67cb-5997-3a0b-a031-a7885b6370c0 | -10.98175 | -46.48315 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0595ba54-424e-3d60-b83e-7465164e5e95 | -14.73716 | -42.90962 | 2026-06-17 04:00:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9208c454-5905-3c60-861d-1c3963da540a | -8.96834 | -46.98705 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45efdbaf-308f-3953-bd82-7a3fcb993745 | -8.95013 | -46.99466 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e673fa5-ac40-3958-89c3-5741c53693b1 | -12.22366 | -52.78924 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8583aeae-cc30-362d-b411-122bda0fbab1 | -8.27316 | -48.21682 | 2026-06-17 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7aea68a-c7e4-340e-9db6-4ed4d0b8975e | -12.17477 | -52.77084 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c2bf4567-8de1-3562-9d1c-ee914955f33d | -12.18675 | -52.78275 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 13cf8611-e210-3ca9-8826-1919c886dec4 | -10.8192 | -44.30783 | 2026-06-17 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e07f3dda-cb48-3c39-961d-8156e8746782 | -12.14741 | -48.45899 | 2026-06-17 04:00:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43c67810-5908-3e30-858f-a37bddd14903 | -11.59673 | -47.44267 | 2026-06-17 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc980aa-6f0a-3994-bbed-bce06804589e | -9.32964 | -45.4772 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e239b5ed-4c98-3a3c-8609-1e14208908b6 | -8.9649 | -46.97559 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58fc44d5-1610-3dc1-b783-eb4f3a2e3d91 | -12.14664 | -48.46286 | 2026-06-17 04:00:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 853518f6-597e-3b6d-863d-a6ccac58edee | -11.06218 | -45.18463 | 2026-06-17 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e39a263-cf23-3d03-b292-4e5028983f92 | -9.2059 | -47.91093 | 2026-06-17 04:00:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7918b316-2abe-3f27-8f8c-5e16a2fc5446 | -10.12379 | -52.1754 | 2026-06-17 04:00:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 30712d2d-daae-3ac7-83a3-ccd1d72b33ca | -8.68099 | -47.8459 | 2026-06-17 04:00:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec4a4dfd-04a3-34a7-a577-e7cef711f387 | -12.75621 | -44.49511 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb91ce08-3a49-30b8-a299-6304a31dedb9 | -12.1964 | -52.77559 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f44d37fc-9f71-3539-b732-3c8184c1c780 | -12.84953 | -44.3698 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 54c2f6be-cfc0-340c-9ad1-322cf872a584 | -12.7257 | -41.80632 | 2026-06-17 04:00:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 13ff94a3-a9b4-3e87-8c1b-3ff89dcc0aff | -12.21806 | -52.7802 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 89ec6e68-afe0-3dbd-a2ff-d15c5476b45d | -8.96556 | -46.97204 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f15502de-44b1-3270-a9d9-7bee97cd0698 | -10.12529 | -52.16816 | 2026-06-17 04:00:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c536aae-f6e3-327f-bc34-29d37f1013a9 | -9.31509 | -45.4744 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45a65924-c2c3-34b8-bfa5-bece3bdb5cc2 | -12.21484 | -52.79502 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 43870ed3-adec-3ddc-bc74-e56ffd041f67 | -13.55673 | -43.43987 | 2026-06-17 04:00:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3787403-f8a5-3894-b7e1-e11845f6bc6f | -10.40143 | -49.45191 | 2026-06-17 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c446875-9a0f-3eec-b53f-02e44d21e850 | -9.29386 | -45.46892 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3cfd431-3523-311f-b154-d3270277b2a1 | -12.65299 | -47.67144 | 2026-06-17 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e52a31e-fd57-36d6-9866-89cc54db0f5e | -8.88444 | -46.97837 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53c251c6-d7fa-3224-b51c-0ed79d766cb6 | -8.94886 | -47.00146 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03d25055-3a32-3130-8fce-22ef97331205 | -12.50535 | -46.3485 | 2026-06-17 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32e13f8a-1acf-3be5-9d73-214a7cee94a6 | -14.06308 | -39.48956 | 2026-06-17 04:00:00 | NPP-375D | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| acbe9bde-9307-3054-a4ad-8bcfd4c29480 | -9.33169 | -45.4819 | 2026-06-17 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 18fd6e42-8729-3243-a884-a09800341016 | -11.88982 | -43.82722 | 2026-06-17 04:00:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9be94a6d-e569-339f-a095-cb8115224eab | -12.83959 | -44.37632 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 1ad1cbf1-ffac-3010-8317-df33a2f37d41 | -12.19482 | -52.78283 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 234bdb04-1b6e-327d-be91-edd78cde3743 | -10.55704 | -46.22945 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16c5b05e-95fd-35d1-bf1b-e05a6ed6ab8a | -11.40895 | -39.52081 | 2026-06-17 04:00:00 | NPP-375D | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7ec16d28-cdde-309c-9088-6c1283993176 | -8.94949 | -46.99807 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48e958f1-c7f8-3184-ada8-4c6fcb0ade76 | -12.20362 | -52.77713 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bc37419-83ca-391a-8f3c-6d26c53ed7b1 | -8.99255 | -46.97709 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5861fa9-9c2f-3f2e-ac9f-bc1872f63aba | -13.09057 | -42.13793 | 2026-06-17 04:00:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dbef739e-1321-3b7a-9eab-8513aff8af68 | -12.1804 | -52.77963 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aa5c864f-4093-3240-9cf1-5dee124ff711 | -10.55811 | -46.22366 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9796fd6-ffa4-341b-a64e-3b27e08211e5 | -13.8154 | -43.65075 | 2026-06-17 04:00:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c7eb7ae-c99b-3479-aa9c-9a3fdd9f4695 | -10.97744 | -47.74382 | 2026-06-17 04:00:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349c4af0-6d2d-30c4-8563-1124cb3ae75c | -8.969 | -46.98355 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8a67561-2183-3407-b295-c238a74e0b08 | -12.84529 | -44.36899 | 2026-06-17 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| dd9d10ab-3819-3a74-8521-59f75e504432 | -8.9919 | -46.98061 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5bb121b9-42c4-3d56-8a23-e6265e9071f8 | -8.56915 | -45.99165 | 2026-06-17 04:00:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e5e88fc-1c12-335f-9c66-4d6eaebaaa0e | -12.2027 | -52.77872 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3924f426-2157-30b7-a892-15dedd83c256 | -12.18761 | -52.78122 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 950ea02d-6f66-36ba-b4c2-370ff7a439eb | -10.56309 | -46.22467 | 2026-06-17 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9bb554f-3e2b-3095-b136-7f906ba373da | -12.65234 | -47.67485 | 2026-06-17 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c061424-336b-3e0b-ba7c-80e5f353133f | -8.96965 | -46.98006 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01a6ce4f-f49b-3db6-aa05-58a39016f450 | -13.55277 | -43.43912 | 2026-06-17 04:00:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2322bdff-889c-30a0-8786-5ed42d929225 | -8.95555 | -46.99561 | 2026-06-17 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 827c97aa-bb6f-344e-9763-18e1e719b7ab | -12.23085 | -52.79091 | 2026-06-17 04:00:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README9.md)
