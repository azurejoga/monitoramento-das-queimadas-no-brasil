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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 651815ad-6b2c-3e9c-bcd8-fad61add7370 | -10.53486 | -69.31647 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32f7f88d-0a61-3bfe-91ff-e721dc9dcd12 | -10.53401 | -69.32088 | 2024-10-02 05:12:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ac7b3ef-7919-30a2-befb-fa0c2006c3ad | -22.11 | -48.46273 | 2024-10-02 05:14:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6257da2e-b5ae-3442-9bd3-b8267f475728 | -22.08271 | -48.46944 | 2024-10-02 05:14:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe058a11-2bab-34ab-80c8-5fea6966b2b4 | -22.08226 | -48.47499 | 2024-10-02 05:14:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdf24ca9-8a16-39b8-ba06-fa0eace159fe | -20.52656 | -46.27758 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3a2d618-855d-3bfb-9603-f14a59eaf2ec | -20.53418 | -46.2714 | 2024-10-02 05:14:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d460f2c-7c66-39b2-9b22-5710a7438a31 | -20.53093 | -46.26641 | 2024-10-02 05:14:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6b5421e4-04de-3c2c-aa19-b9b01a671092 | -20.53036 | -46.27359 | 2024-10-02 05:14:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| daf796ee-1f81-3f6f-a7ba-6b6c99360bc4 | -20.52703 | -46.27115 | 2024-10-02 05:14:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 428ac160-be51-3934-8551-050114f83b54 | -20.52606 | -46.2844 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| add0c3aa-bb84-37be-93ed-94f652a7072c | -20.5233 | -46.27211 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2aeaab51-5f3a-3818-b041-1c2c5586048c | -20.52279 | -46.27858 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a486116-74cc-3f19-9667-8982912d52a6 | -20.51951 | -46.27583 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae2741a5-628f-3a89-8a9b-f7c0258622ff | -20.51902 | -46.28261 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a9e4e06-7d12-3930-a534-bd444557f228 | -20.51566 | -46.32882 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bf1964bd-725a-392c-994d-cad84669500e | -20.51219 | -46.32227 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55a597de-e811-34c0-82a4-7882795a5fdc | -20.5116 | -46.32976 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 008179e6-c87b-3984-950d-35504846011a | -20.50584 | -46.312 | 2024-10-02 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4af9d213-06b3-3bc6-92bf-2986e3853936 | -22.20753 | -46.00077 | 2024-10-02 05:14:00 | NPP-375D | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9675b0e7-7ee2-37b7-84ab-9ce2ea608790 | -22.20693 | -46.00276 | 2024-10-02 05:14:00 | NPP-375D | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 806d28f1-2f4f-3f50-9955-17db39431ada | -22.20031 | -45.99835 | 2024-10-02 05:14:00 | NPP-375D | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98d740de-29b8-3986-8222-6127c5cc60a4 | -22.19972 | -46.00042 | 2024-10-02 05:14:00 | NPP-375D | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d0c6efd-279c-34d5-ae8c-468f06071a03 | -23.50819 | -47.2215 | 2024-10-02 05:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 29a5c50d-36cd-3172-8164-e494a3c80d79 | -23.50777 | -47.2278 | 2024-10-02 05:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 79df0e4a-0068-3385-816a-196b84e05ccc | -23.50734 | -47.23421 | 2024-10-02 05:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| aa8f39d0-3c1f-3fc2-be6f-0ef8b724becb | -23.5017 | -47.21418 | 2024-10-02 05:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 97d3d9c8-673c-3076-ae43-e9f3f88fd226 | -23.50127 | -47.22065 | 2024-10-02 05:14:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8b92a451-2c46-3d27-9328-a3047a49cf0d | -23.16003 | -46.3246 | 2024-10-02 05:14:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8a4fa850-6ae2-339a-aa41-c60137b17a20 | -23.09123 | -46.37621 | 2024-10-02 05:14:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3cbdd60d-3557-30d3-aeae-947aa1cf22df | -23.09086 | -46.3824 | 2024-10-02 05:14:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 46bc23bb-3905-3ff8-8edf-39645eefdce6 | -23.09029 | -46.37803 | 2024-10-02 05:14:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0fe3eb6b-ac94-30b0-a085-57cf458805af | -23.08989 | -46.38405 | 2024-10-02 05:14:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c3546e68-8e76-39db-a7d1-9272a7cdbbe7 | -23.04173 | -46.88441 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 17dc5f0e-8059-3a92-ba7c-e1810bd643bd | -23.03856 | -46.88297 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a6ae2349-2d90-3aba-84e6-b75383171278 | -23.03813 | -46.88971 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 41843ee6-44f8-353c-8318-dc65575fe771 | -23.03513 | -46.87749 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 687a9c28-7099-37af-aa5a-16ae75fc4490 | -23.03461 | -46.88503 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f6431b1e-f532-3252-b0d1-165485a0c9ca | -23.03147 | -46.88304 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8bc632b7-fa84-3b17-b3b4-26992105af0f | -23.03106 | -46.88969 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fd714138-0365-31d0-b7a0-f1622f6bd5d7 | -23.02754 | -46.8848 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 37cab58a-7ffa-33f8-a088-9a9682d41f6e | -23.02711 | -46.89114 | 2024-10-02 05:14:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7e1fbb75-8bd7-34e8-8dc7-dfa71ba59b02 | -22.716 | -46.68025 | 2024-10-02 05:14:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 8577a704-b32d-314d-bca5-dc36f541402e | -22.71563 | -46.68563 | 2024-10-02 05:14:00 | NPP-375D | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| fde3fb0a-dce4-38ba-9a57-ddfcc493ac46 | -19.47486 | -46.89181 | 2024-10-02 05:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca8e5c0b-449b-3bd0-aee7-e97bca8ffbf7 | -19.24018 | -46.86167 | 2024-10-02 05:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6178c354-b9ac-3700-ad67-3cbd3907b075 | -19.23498 | -46.8602 | 2024-10-02 05:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6baa510-72df-3ce6-9f97-5d7fc7b07c3b | -19.23446 | -46.86658 | 2024-10-02 05:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac80488a-b182-383c-86bc-ecdeafff421e | -19.23337 | -46.86094 | 2024-10-02 05:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6467fdef-3aed-32fc-a681-20d475158ace | -19.23282 | -46.86723 | 2024-10-02 05:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1cf384d7-1f72-3989-9b70-51c290e40485 | -18.98351 | -47.29528 | 2024-10-02 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c699cb30-a3fd-380e-9ec2-d2ddba691a76 | -20.6493 | -47.0432 | 2024-10-02 05:14:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d04e4fe4-7df9-334a-8265-072d8a8fda0e | -20.64833 | -47.04083 | 2024-10-02 05:14:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a86e62d1-3185-334b-8ddd-3253a785fdb8 | -20.6478 | -47.0474 | 2024-10-02 05:14:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58d4b84c-fef3-3acf-9289-6df731600b0d | -20.64249 | -47.04213 | 2024-10-02 05:14:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d09e1795-b51c-3c34-9561-a52046c1b1b6 | -20.63448 | -46.77873 | 2024-10-02 05:14:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75758139-61ba-3263-aee1-98575e9f5626 | -20.6275 | -46.77861 | 2024-10-02 05:14:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25649cb0-d34d-3285-88b9-f99898e37724 | -19.93085 | -46.91349 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6dab13f5-06a4-36e7-ac28-5cc7236a187b | -19.93047 | -46.91494 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1a0cc72f-1d51-35f5-b014-89be3d77c13b | -19.93035 | -46.91986 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3888e357-58ed-3cbd-a6fa-3e27e6837b4e | -19.92993 | -46.92137 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6e5eec0b-0849-356b-9194-ca516999720d | -19.92985 | -46.92633 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 594e61d9-3de7-3d06-8aa2-8b931fdfb3a1 | -19.9294 | -46.92777 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 365ef275-6e05-3f5e-85da-00149793de29 | -19.92934 | -46.93298 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| caf996b6-515b-31dd-b6c5-5efe199c4f3a | -19.92884 | -46.93438 | 2024-10-02 05:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a75ec71-6058-310d-9cbd-c14ea62133b2 | -19.76195 | -46.61001 | 2024-10-02 05:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 548779f7-959e-30af-aefa-17730a44ce83 | -21.55123 | -47.79664 | 2024-10-02 05:14:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e8c124f-4955-3089-85db-82cabd4bb921 | -21.55074 | -47.80253 | 2024-10-02 05:14:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72832daf-9c75-389e-8cd2-ccfa6826ee49 | -21.54902 | -47.79284 | 2024-10-02 05:14:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19086442-3d5e-3dd7-a366-9ad5933d5be1 | -21.54857 | -47.7988 | 2024-10-02 05:14:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98ce496c-c215-3733-90d2-376ba5b83100 | -21.54507 | -47.79061 | 2024-10-02 05:14:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc3c64cf-f9df-3af2-9b96-c9a498b6d8e7 | -21.29017 | -47.61837 | 2024-10-02 05:14:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0cba1ae4-fea7-396d-9458-bd8009afa5df | -21.28977 | -47.62334 | 2024-10-02 05:14:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7504b99f-d622-315f-9cf5-426e01898348 | -21.28938 | -47.62833 | 2024-10-02 05:14:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 13391bf4-353b-319b-949f-d56ed0c72c10 | -21.28344 | -47.61867 | 2024-10-02 05:14:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aa8264fe-acf4-3791-a18d-edb1e9e10973 | -21.28305 | -47.62367 | 2024-10-02 05:14:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c3a66428-b7d0-375b-ba63-9d9b4703c06d | -21.28267 | -47.62844 | 2024-10-02 05:14:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ed3904ef-2d4d-367e-8ee1-a3b713d60ea1 | -21.89904 | -48.47596 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0965d1b7-5665-36a4-914c-4bf5878b0ea3 | -21.89404 | -48.47366 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fb73318-8b01-36bc-b780-2673b3160332 | -21.89366 | -48.47852 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dbd74923-39a3-39c0-80bf-201305fed062 | -21.8926 | -48.47608 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7686ba62-388a-3055-b8e3-7325fbaed235 | -21.89219 | -48.481 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 749495da-1eff-3561-b961-fdff0ce1c3f9 | -21.88724 | -48.47855 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6d48816-c326-3dab-9b48-a74de201cbc9 | -21.88686 | -48.48344 | 2024-10-02 05:14:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acaf84de-1a46-3711-ba32-1633e548f66b | -23.81944 | -47.6464 | 2024-10-02 05:14:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8fb6977f-d78d-3a1c-aed6-c671b1e6cfe2 | -23.81865 | -47.64484 | 2024-10-02 05:14:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 6c6c7e54-34b4-3375-93c2-a57b951c6eca | -23.81822 | -47.651 | 2024-10-02 05:14:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a47685ee-2dbf-347e-b7e3-6eb6f9ce6b0a | -23.81267 | -47.64537 | 2024-10-02 05:14:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 391cf7cc-6f94-3491-a6d1-0fc5cdf3a717 | -23.81188 | -47.64384 | 2024-10-02 05:14:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24e520f6-1572-35ff-8e74-9dc7f7ec5a6d | -18.9879 | -48.35806 | 2024-10-02 05:14:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4193fa0-0080-3337-99ce-a8603219b4ac | -18.98745 | -48.36301 | 2024-10-02 05:14:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ca47caa-a2dd-379a-9ab2-52af80ab3f80 | -18.9842 | -48.3571 | 2024-10-02 05:14:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57d22ec4-22fb-36dc-b5ce-49a75b417f15 | -18.98371 | -48.36212 | 2024-10-02 05:14:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f58bad5-61c9-3a54-9628-dcb55ced7986 | -18.98165 | -48.3576 | 2024-10-02 05:14:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f68a5f7-06f3-3e7a-b50b-a42258b85a4e | -20.64367 | -48.74964 | 2024-10-02 05:14:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 368cb304-7f12-370e-a534-dde1533b729b | -20.64176 | -48.75047 | 2024-10-02 05:14:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b5fd250-5598-321f-89d7-d3ffcbc4a877 | -20.63701 | -48.75413 | 2024-10-02 05:14:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 293f6836-e42c-3832-a170-358e44e8d3ea | -20.63514 | -48.75486 | 2024-10-02 05:14:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 61b11525-eace-3814-a9a1-ac3bba0768d1 | -22.39493 | -49.29819 | 2024-10-02 05:14:00 | NPP-375D | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| c6d4bf94-21cd-33a5-bf4e-6a1e856c9a47 | -22.39005 | -49.28279 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README162.md)
