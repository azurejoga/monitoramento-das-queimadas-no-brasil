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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb66afaa-c084-3351-8693-b661d71affdc | -12.2741 | -43.5152 | 2026-05-22 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 89195cc7-2301-35c8-9f9b-b061d99bc216 | -9.2855 | -45.483 | 2026-05-22 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8af693d6-4f31-316e-b0da-ce5ac08795b9 | -11.6123 | -55.3283 | 2026-05-22 00:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 55678507-5f0b-3777-81de-b5da621d6f23 | -9.3045 | -45.4809 | 2026-05-22 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 08734900-38f0-304b-aecc-babe80b4551a | -9.3041 | -45.5036 | 2026-05-22 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cb577ec0-dd2d-324b-9961-896f63e83654 | -9.2855 | -45.483 | 2026-05-22 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4b83beb2-d2ce-3036-8e6c-a43f6807047b | -9.3041 | -45.5036 | 2026-05-22 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8d81260a-ff8c-3777-9c79-a843d060952a | -12.2741 | -43.5152 | 2026-05-22 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 748c5218-fe68-3c3e-a46c-5e10d8c736dd | -9.3045 | -45.4809 | 2026-05-22 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 24c545e7-9a00-3a37-b52a-626cd187a553 | -12.2741 | -43.5152 | 2026-05-22 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 63402ca1-a192-3b89-a039-cdb2817f6997 | -9.3045 | -45.4809 | 2026-05-22 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| fab60b72-ee35-35ae-bc45-4dedc6722d9f | -9.2855 | -45.483 | 2026-05-22 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d0deb824-f1df-3f61-b7d4-34b78673ab50 | -12.2738 | -43.507801 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1734d958-2093-398a-ab87-e18ab7e1787a | -5.9562 | -43.481998 | 2026-05-22 00:22:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78afd2d2-81b7-3f87-ab5c-b5096ad8d954 | -5.948 | -43.491501 | 2026-05-22 00:22:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8c9ceab-11ff-3655-b866-4e697182579a | -12.2656 | -43.516998 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24160505-0833-3aaf-8f74-a8b6a4da31f0 | -8.5576 | -45.991199 | 2026-05-22 00:22:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a15d2c43-0f16-3725-8eaa-b1d8d0899c02 | -5.7685 | -45.1353 | 2026-05-22 00:22:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b9a34b3-886d-3dd8-a7d3-b6ba9702ba6f | -12.264 | -43.509998 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b64303d1-a79e-39d8-9157-4555e64e230a | -11.6114 | -47.9006 | 2026-05-22 00:22:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9105645-e0c0-355b-abfb-5f442ef3db6e | -8.7226 | -48.327099 | 2026-05-22 00:22:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 030235ab-1e30-3f41-87ef-fcde42c30453 | -12.814 | -44.867901 | 2026-05-22 00:22:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a89ecaf9-fb95-3dba-a13d-25f65c694ee9 | -8.7186 | -48.309101 | 2026-05-22 00:22:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d488f03-28d3-304c-8599-f0ae017e43ec | -5.767 | -45.128399 | 2026-05-22 00:22:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9f20c54-895b-3b1f-bd8a-1de23964e849 | -10.7935 | -49.404598 | 2026-05-22 00:22:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68a5a018-346d-3f6a-8659-084a6fef752d | -10.489 | -49.364101 | 2026-05-22 00:22:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 698fe9bb-97ab-3747-a3e8-578c79f876b4 | -12.238 | -44.265301 | 2026-05-22 00:22:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a46dd5a4-8905-301f-ba79-bd0d7e6ed55c | -8.7128 | -48.329201 | 2026-05-22 00:22:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f12cc06-8508-33ac-baa4-ea90c0f3f9c9 | -8.5544 | -45.976799 | 2026-05-22 00:22:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4ba899f-ade9-3b56-afe8-17236bfab6c3 | -6.5659 | -47.900501 | 2026-05-22 00:22:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61c70bb8-01ad-3f0c-824d-37474f828dc7 | -8.1191 | -44.187099 | 2026-05-22 00:22:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47a529c7-449a-39cf-ad43-79aabe521ace | -12.0002 | -45.141602 | 2026-05-22 00:22:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3c40092-4bc9-3319-b4d8-406338b82678 | -8.1176 | -44.180199 | 2026-05-22 00:22:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d29d4bc0-d3a8-3f20-9dd4-d1fef52d4665 | -11.0373 | -46.7995 | 2026-05-22 00:22:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f135d2b-f990-3798-b45a-37109ccfdf2b | -5.7768 | -45.126202 | 2026-05-22 00:22:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c48c896e-8151-3ccb-971b-13f27807f9a5 | -5.9578 | -43.489201 | 2026-05-22 00:22:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0137266d-a2e2-310b-9c7b-a49c8587490a | -10.4867 | -49.3531 | 2026-05-22 00:22:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c2bcff5-bc99-32ac-8aff-fb1a1baa28e2 | -10.3996 | -46.745602 | 2026-05-22 00:22:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86d4d00a-da36-39c1-8790-92a91b2c8734 | -9.2898 | -45.491199 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 280ff882-c74c-36c6-9d82-1a8dc2c38b0b | -9.2996 | -45.488998 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79e1f09c-0604-3d5e-8a21-0bfb7efa9ab5 | -12.2722 | -43.500801 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4255f122-ab35-3c47-870a-baac0d151f35 | -5.9251 | -43.481499 | 2026-05-22 00:22:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7986e557-2105-329c-b296-9922c584e896 | -6.5677 | -47.9086 | 2026-05-22 00:22:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33674778-8cbc-39b5-b1ec-0614330a58b0 | -5.9234 | -43.4743 | 2026-05-22 00:22:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d676b950-a9ac-3e9e-b282-f7867689dfcf | -9.298 | -45.481899 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06240987-5331-3478-a17b-ea3bca707e6c | -12.2365 | -44.258301 | 2026-05-22 00:22:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27576508-72b5-3690-904e-2b81d8e707c9 | -8.9262 | -46.911499 | 2026-05-22 00:22:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44adea7b-e8ee-304b-8ac0-32c0dd3094e5 | -8.116 | -44.173302 | 2026-05-22 00:22:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7baaa19f-e547-39af-8cf3-f962f4c68706 | -12.2624 | -43.502998 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80f8db34-07a1-3534-8502-b86dade2c6f4 | -9.0734 | -49.673302 | 2026-05-22 00:22:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dad7e798-95d5-3062-9ea7-ba0f5531ad42 | -7.6421 | -45.307899 | 2026-05-22 00:22:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6067b97d-b849-37a4-bfe3-c0dd807fc5e0 | -11.0356 | -46.791401 | 2026-05-22 00:22:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3145a808-747a-3c35-ba15-a32b16711905 | -8.9279 | -46.919201 | 2026-05-22 00:22:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2ca851-b435-3929-be4e-d3d274c194d3 | -7.6405 | -45.300999 | 2026-05-22 00:22:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 003affe9-6801-3b92-9366-a22d5072e64f | -5.9464 | -43.484299 | 2026-05-22 00:22:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d3638d5-2387-3e85-8451-8bd5e0805c96 | -9.3094 | -45.486801 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf5e878c-47e4-33d4-ab75-107f74fbb1b4 | -12.277 | -43.521702 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46eb1c4b-111c-3a49-8ad6-3e47e138f4bd | -8.7206 | -48.3181 | 2026-05-22 00:22:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9430494a-7baa-35a8-8a1f-e506389da2d8 | -9.2882 | -45.4841 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90a56ad1-579e-3407-8c3a-c8a2041b6967 | -5.7783 | -45.133099 | 2026-05-22 00:22:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37f222af-3caf-39f1-b18d-d871467cf076 | -11.0338 | -46.783298 | 2026-05-22 00:22:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8506183d-dbd7-3e17-962c-92972859016d | -9.3011 | -45.495998 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d846bf2c-0c0b-3add-8e97-0773fb76a76a | -12.2754 | -43.514702 | 2026-05-22 00:22:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 509d52ee-e7e1-3643-a8f5-eddabcbfc796 | -8.7108 | -48.320202 | 2026-05-22 00:22:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 185d4921-0af1-3c49-bb00-356ac6e550be | -10.644 | -42.293301 | 2026-05-22 00:22:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4c6f51c2-a2a2-353b-ba75-ac26b53f0331 | -9.2866 | -45.477001 | 2026-05-22 00:22:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32f15416-d2bc-3b68-a581-8cf13f71308f | -8.556 | -45.984001 | 2026-05-22 00:22:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 402ec8bc-8a24-318e-962c-1a3d0a0361ba | -12.2741 | -43.5152 | 2026-05-22 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 9760375a-4b47-3c00-aa8d-6ef47d10e418 | -8.7211 | -48.3222 | 2026-05-22 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 278add98-fe14-39d5-972e-a57d3fea9dfa | -12.2741 | -43.5152 | 2026-05-22 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5a384ab8-7116-39e7-8a5a-e692aa5ac65e | -11.6123 | -55.3283 | 2026-05-22 00:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 067d6ca6-af65-37db-8028-fc695a3eb21a | -12.2741 | -43.5152 | 2026-05-22 00:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c11820e8-1f3b-3f17-affc-65d89a0f0fca | -9.3045 | -45.4809 | 2026-05-22 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0c925309-ab49-3471-8f5d-e4425754a36c | -9.3045 | -45.4809 | 2026-05-22 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e61f23cf-4f59-361f-a87a-b8fc9ffaca65 | -12.2741 | -43.5152 | 2026-05-22 01:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e11d6c99-bab7-3a4c-862e-ad2bd6c5c554 | -12.2741 | -43.5152 | 2026-05-22 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e703a364-da51-3f19-969b-49e0832bdd9e | -9.3045 | -45.4809 | 2026-05-22 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 77c3e811-ed06-33ea-90b7-2dbb7d01b033 | -12.2741 | -43.5152 | 2026-05-22 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 2b50c6bd-af6f-394a-8c00-da02dead27a9 | -9.3045 | -45.4809 | 2026-05-22 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| b6f6fbf9-19d6-33f4-9c01-9376fe8e2484 | -9.3045 | -45.4809 | 2026-05-22 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 1dfbc4a0-d623-382c-aecf-6cf6d90a7942 | -9.3045 | -45.4809 | 2026-05-22 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c269d1db-2931-3906-93f6-caaea32059ee | -9.3045 | -45.4809 | 2026-05-22 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a5902bb6-6627-3e0c-b4eb-58dec9e3fd81 | -9.3045 | -45.4809 | 2026-05-22 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a317048b-a23e-30f9-83cb-373d5af1edae | -9.3045 | -45.4809 | 2026-05-22 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1374f164-0ce7-31d5-b2b6-fd9977983a1f | -9.3045 | -45.4809 | 2026-05-22 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6110c558-4a16-3b1e-9181-7626b7c288c2 | -9.3045 | -45.4809 | 2026-05-22 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 62822b50-92cd-3cfe-ad6b-8e2923c6c9c3 | -9.2855 | -45.483 | 2026-05-22 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 960dd84d-13d2-31d0-9cd0-a3df8938a4cc | -9.2855 | -45.483 | 2026-05-22 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8efc6641-c51c-3c08-a5dc-372f4683eaa7 | -9.3045 | -45.4809 | 2026-05-22 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2fbbd132-a069-34f4-b449-4e40ac921dca | -9.3045 | -45.4809 | 2026-05-22 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2ad2d1a1-868f-30e6-9545-49c5ceaf6ae7 | -9.2855 | -45.483 | 2026-05-22 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6814127e-52ac-3d62-9ae1-9d5ca9c23d00 | -5.7775 | -45.13778 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9c19745-fd52-3b32-9088-82d34c1b9a1d | -5.76595 | -45.13079 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7292845-5e9a-381f-b62f-3f3a94c71d71 | -5.9501 | -43.49126 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ea4f065-aba0-3291-9a9e-4d01868baf0f | -5.76786 | -45.13128 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31d949bc-ee60-3712-ae22-f8640901483f | -5.92425 | -43.47467 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b63515e-b17f-3d51-903b-8580466dcd08 | -5.77409 | -45.13226 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5d59191-b15e-3864-b07a-79a76294976b | -6.72184 | -36.98315 | 2026-05-22 03:45:00 | NPP-375D | VÁRZEA | PARAÍBA | Brasil | 2517100 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac149ed0-09ff-33a3-839e-5215fd485d88 | -5.77218 | -45.13182 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d08e3faa-6240-3b61-8c5c-ef74abe3f683 | -5.95568 | -43.49228 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README2.md)
