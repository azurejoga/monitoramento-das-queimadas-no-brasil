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
| cea0e351-af96-311d-b63a-eef656672d1b | -6.35409 | -46.16577 | 2025-08-03 03:36:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48b78db7-4a6d-3f3c-8aa9-19e3ee2b7df3 | -8.00647 | -43.15239 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 1e2d2d6a-62ab-3f17-b295-987a80d5c94c | -7.96095 | -45.11821 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75223244-b782-3f1e-857a-e293063de73e | -8.01932 | -43.14119 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e843b4dc-0291-344b-8943-fb06760694c7 | -12.09841 | -42.9217 | 2025-08-03 03:36:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6547d93b-833e-3a26-b8e2-ef2e07ab38b1 | -8.01174 | -43.15336 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9af6118c-ce5a-3e4f-9cc8-a638ddad7273 | -6.67543 | -44.35364 | 2025-08-03 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3dc6e3c-85a1-30ae-91c3-157c78fdbe6a | -7.99467 | -43.18834 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| dc50985a-0c2e-326a-9e21-d99d625f0d1d | -8.01642 | -43.15771 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 16c8913b-a4fd-334d-87f6-35f5dd2b58e1 | -8.42707 | -47.46393 | 2025-08-03 03:36:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f79b716-cd5d-3db4-ba39-17a82475e3a8 | -7.9601 | -45.12265 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7caef205-9cee-3461-94e5-c8a0e97098d9 | -7.99408 | -43.18601 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 6c571d80-e641-31bb-be35-04110f02668a | -9.39407 | -45.50684 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1871d430-d293-3b30-880c-4c5bafe398f0 | -11.76632 | -44.98115 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3447be20-d138-3b90-9dc9-bae5a59d4da1 | -8.00705 | -43.18001 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ee2262ce-1ac7-3055-97e1-146a3c2af4c9 | -8.00124 | -43.17678 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 6936079d-43a6-34a7-b505-a116455a4a93 | -7.87584 | -45.53548 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be25c531-a349-3166-b54c-ee6687620955 | -9.39585 | -45.49773 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 826d6808-2a0a-306d-9c22-9004947f6d39 | -7.95925 | -45.11574 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48de6895-6d08-3484-9c0f-c8fc424f0022 | -11.7766 | -45.01675 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 050bea08-b26c-3de9-9e95-4ef8123ef39d | -11.77627 | -44.9967 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 992e079f-63f8-333d-802b-6bdec1cb9ce7 | -8.87895 | -44.79409 | 2025-08-03 03:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 765d57f8-87ad-3c8a-bed9-26c4d132a9fe | -7.88168 | -45.53352 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3780e68-12f2-3d62-97b6-caad4f2e6976 | -7.75935 | -45.11162 | 2025-08-03 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de770f5a-fe9c-385c-a436-dd1add1f6998 | -11.77994 | -44.99986 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eb1468f-c955-34a1-ab04-f67ae86b3eed | -8.00997 | -43.16343 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a51210a9-0d9d-3771-bb94-6c9ebbaf1d1a | -8.01546 | -43.15874 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d7c34160-995f-3a9a-af09-7b76ddaef807 | -7.99878 | -43.19015 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e9ad37f7-5ff9-32e9-9692-7c8461292883 | -7.99526 | -43.185 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| fa343e1b-4ab6-3c6a-ab91-abe85cf7b2ab | -8.0191 | -43.13897 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ab7d25d-2b1b-3101-8bce-9d513c1b0336 | -8.00492 | -43.15682 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 4e312427-700e-3a46-abe2-c6cd85237ad9 | -8.00529 | -43.18998 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a6f73474-f72a-3d8a-bd66-c09fdb3d9d3c | -8.017 | -43.15436 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| efe30085-8941-3652-b3dd-abdc91bc4758 | -8.02376 | -43.14319 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1218b911-6d58-3484-8958-cd6b4b6babec | -7.95679 | -45.12915 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78e9b7d4-52f1-3a17-8057-087126649579 | -7.88286 | -45.53189 | 2025-08-03 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 79ffec7c-d157-385a-b4e5-2cb3f1829b38 | -11.77114 | -44.98597 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d21c5d-155b-30e2-8293-f53b22c3b61a | -8.00176 | -43.17907 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 2f539a42-69fd-327e-888a-2fa60daf19b1 | -8.02029 | -43.13244 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a30da25a-e77a-3b0a-9bbd-02f005c77406 | -12.03092 | -44.02016 | 2025-08-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5145dca7-f07a-3aee-98ee-f513e0d78bba | -8.01729 | -43.1488 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c6fe386c-9c16-3892-891d-991c1fb9db28 | -7.99998 | -43.18914 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| bf2ca698-faa3-36c8-880b-257b3ca32bff | -7.96089 | -45.10677 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 422a1f34-bbfd-364f-aabe-ad3230e3680d | -9.58792 | -43.84007 | 2025-08-03 03:36:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68d767b2-1bf5-3258-9cbc-2aee80c9558b | -6.35514 | -46.16002 | 2025-08-03 03:36:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b64f2c9-78dc-33bc-8127-8c6db0814e48 | -8.01759 | -43.15105 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 14132728-25bb-3ecc-9a37-2f9e9555e648 | -7.99816 | -43.1935 | 2025-08-03 03:36:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 45058d20-cac4-3270-935a-b6b58411de45 | -9.39334 | -45.49968 | 2025-08-03 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5845659f-139e-3591-b2c4-1f14b68c6c6c | -7.96252 | -45.09785 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32b9ee5a-2a8a-3f6c-99a4-a4e6057ed207 | -11.80521 | -44.93007 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f5ba1c9-dd33-37b4-b1bb-863b382b3269 | -8.00468 | -43.16253 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fabea525-b703-3a92-948c-f0a9eff901ee | -12.03033 | -44.02329 | 2025-08-03 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 608fcc3c-a111-3ec3-b0df-55d0266108f0 | -8.942 | -46.74794 | 2025-08-03 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b150760f-070d-336d-a953-466b913554c4 | -10.33788 | -44.9045 | 2025-08-03 03:36:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8243852-c4fe-3a13-af7b-c275d19e0192 | -11.77218 | -44.9879 | 2025-08-03 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99ca01b0-0d42-33e1-8dd2-d62f4bab2b63 | -7.96444 | -45.12116 | 2025-08-03 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcaf226b-da95-36c1-8663-6d909ba2949f | -8.05251 | -43.10468 | 2025-08-03 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3113f6dc-5683-340a-9af4-2689b562cf43 | -11.94612 | -44.96801 | 2025-08-03 03:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3461a4a8-16a3-3b3c-9768-12334ee319df | -13.6816 | -41.36827 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 76ed3366-69da-3918-a240-963642d4d0d5 | -12.64709 | -44.50286 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e103910-d484-3e1b-8cf7-71051e8bd064 | -12.6438 | -44.4916 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d5c9a1b-c42e-3984-8192-da5fbdc350f5 | -12.65305 | -44.50057 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d688d99e-3505-30f8-903f-4d202a5c764e | -12.64975 | -44.48932 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9144eba-9429-3ebe-adc8-047c180d30df | -18.22905 | -44.70443 | 2025-08-03 03:38:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fe94622-b168-37a8-98eb-481fb52d18df | -14.17343 | -45.46075 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20747a7f-d0f4-38a7-8c84-8d8695c16f83 | -16.82951 | -42.87283 | 2025-08-03 03:38:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fdeb1f8-909b-37d5-8ef7-09fc42c9b68b | -12.64046 | -44.5086 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bf38b03-c513-392c-9a28-4cd780c15c25 | -12.67157 | -44.49032 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fe7eb50-4587-394c-9c25-659b6377c888 | -16.67897 | -41.35379 | 2025-08-03 03:38:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eba8bda8-3477-3c52-bc1a-87a5a406f8fb | -14.16071 | -45.43964 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e6fe757-5e2b-3e2f-a546-42dc8623fd9d | -12.64313 | -44.495 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8268fae7-3099-3061-87ee-96d9357d46e1 | -19.14197 | -43.56741 | 2025-08-03 03:38:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0aeae82-1db2-376b-a864-528c64c9b01c | -12.42018 | -43.48849 | 2025-08-03 03:38:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7ebe337-d408-300a-861a-df340206fe92 | -12.67994 | -48.09472 | 2025-08-03 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4a536d3-4ff4-30aa-be0e-21dd517b1be5 | -12.69594 | -45.03628 | 2025-08-03 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd084794-7121-31cb-b9f9-1aaab299ecdf | -14.16151 | -45.43528 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a21db228-eaec-3800-92bd-4a2eb6b88755 | -14.15598 | -45.43476 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 471983f7-1d60-342e-acc5-ae91e80168a8 | -13.69858 | -41.3712 | 2025-08-03 03:38:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc2c7431-a729-332e-a922-17c01b5ee30a | -12.41174 | -47.06826 | 2025-08-03 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f996cea-28ae-3745-8a95-8fc9b5b64f92 | -18.83863 | -46.45095 | 2025-08-03 03:38:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e8d56037-bf75-3b48-8976-bf0d1c060242 | -14.1702 | -45.44859 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7384ed0-3fcc-307e-a5f1-bff2e750bfc1 | -14.1396 | -45.43109 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 175a7c1a-974f-3b31-a73c-7392e293b78b | -12.65768 | -44.50508 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2439bfed-18c3-3be8-9358-646a34beb867 | -13.67226 | -44.22717 | 2025-08-03 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50051308-5537-3b25-8cfd-d787763cf2c7 | -15.5882 | -48.50878 | 2025-08-03 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d039e02-c25a-3d19-8b54-cbb0312f22be | -19.62453 | -43.17446 | 2025-08-03 03:38:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1a16d4c2-3a3b-37d6-ac03-0e7c3dcf1ae6 | -12.6709 | -44.49373 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2703f551-dec8-382e-9586-b46e3f69471e | -19.20925 | -40.0955 | 2025-08-03 03:38:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c98a223-c46c-3f06-8640-0c3d77953278 | -12.64246 | -44.49839 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8f7c2fa-8a70-3b42-b6d9-5437c85f6e48 | -19.62279 | -43.1725 | 2025-08-03 03:38:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f0007a2-113d-3e5c-9ca4-eb9ce9d97acb | -14.16876 | -45.45668 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 598c58c2-e36d-318a-94eb-b73082b7e654 | -12.66098 | -44.51641 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 169fceb0-16f3-3c1a-94b1-1fee8904dd0a | -14.13886 | -45.43479 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e53274f4-cb94-3d35-a0d8-c32a9052016a | -19.498 | -43.83202 | 2025-08-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbdca0c7-c057-3945-873a-abb740c6ae53 | -12.66628 | -44.48922 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a7b4be8-8aeb-3086-9d70-6d69fcbb766c | -12.65437 | -44.4938 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e82488d9-b752-3c7f-ad8a-efa79e45f488 | -12.65434 | -44.52214 | 2025-08-03 03:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32b3674a-9966-316c-9168-cf67f74a18ce | -16.67828 | -41.35765 | 2025-08-03 03:38:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 06fc4325-18f0-3005-9ef5-70a15c22a1d7 | -18.83328 | -46.44977 | 2025-08-03 03:38:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c02de9c3-0026-3449-9379-7ef10b2fc8ad | -14.16698 | -45.43646 | 2025-08-03 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
