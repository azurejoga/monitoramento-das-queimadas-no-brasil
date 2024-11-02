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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb919ffd-2a33-325f-902a-9aef352aa454 | -3.11247 | -54.29386 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cdebf6df-ef9c-33b4-8889-586a5ee6fd8e | -3.11193 | -54.29733 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be5125a3-c56b-3752-9fd8-05e94a9d1ee4 | -3.11185 | -54.276 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7026eaf5-a8d8-3aa1-abe8-ae4b0a2256aa | -3.11131 | -54.27948 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 322cd8ac-e47e-325d-889d-9b4495d6733d | -3.10916 | -54.29335 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae3ae1d6-c25b-32ef-b24a-d79b38007571 | -3.10862 | -54.29681 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f1cd232e-0a8c-31e6-86e6-91b022e11aa6 | -3.10853 | -54.2755 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19301953-0582-321c-a093-2337baa2c4c2 | -3.10799 | -54.27897 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04bc7c64-5628-314a-b9e3-327848b9b9cf | -3.10746 | -54.28244 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c623914-78ea-35e6-92b4-999e0e27459f | -3.10692 | -54.2859 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee26891b-99fd-3321-8bc3-2b02d127b24e | -3.10638 | -54.28937 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f013b3a6-802a-390e-a21c-647b894a420d | -3.10584 | -54.29284 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cc6052fe-5352-3635-9f0b-7da0b663f3f0 | -3.10414 | -54.28193 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1054de00-b96f-35d4-a4ce-60a4be4184c5 | -3.1036 | -54.28539 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f81befad-8422-3530-a196-27fecec67fef | -3.10306 | -54.28886 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad1d7710-682d-3d69-8b73-fd5fe10cb75c | -3.10252 | -54.29233 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 424eb40d-51e5-30d3-a617-9fa3496f12bb | -3.10244 | -54.271 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 428c631a-0a1b-3bc8-8227-09c9301fd349 | -3.10136 | -54.27794 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 133a8843-30b2-3ec6-93ed-107b73a8ab1e | -3.10082 | -54.28141 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5ddf78-f604-3790-98f1-547192029195 | -3.09804 | -54.27743 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91abe51a-51f1-3dd4-b966-0191b13018c2 | -3.09751 | -54.2809 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a46cae8-0ec8-39e5-bb1c-0e8bed0bbc56 | -3.08982 | -54.54865 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ec9b56d-049f-357c-a0ac-453e84477ca0 | -3.03832 | -54.48777 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc6d1c70-f87d-3a48-8d1f-40fb0f9e479e | -2.98681 | -54.55399 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13a7bf35-1615-33f6-84f3-e1b7dd284ccb | -2.9835 | -54.55349 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fdeb8e2e-095f-375c-8fc4-c11a10fa797e | -2.98181 | -54.54265 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f493efbb-fcba-3455-8419-f84aac9c3645 | -2.98127 | -54.5461 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87157223-60fd-31ca-b90d-9ddff97a16ac | -2.97486 | -54.91788 | 2024-11-02 05:04:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 219d3e6f-b992-3305-99ef-bb80fcb168c2 | -2.93444 | -54.36572 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04463b18-9e48-30cd-93ad-5f9af6d50e59 | -2.83662 | -54.55898 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837c3e8c-fea8-3a7f-b788-482eb76927e1 | -2.83332 | -54.55848 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d80c102-2595-393a-8c4f-150a27ef54d0 | -3.18468 | -53.84998 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0e6a805-37cb-3f95-b690-18c970e144eb | -3.18413 | -53.85351 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 242f4327-ea56-318a-90f2-ac6171f027ce | -3.18134 | -53.84945 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9861b2dd-5f9a-36d2-a3c5-82553b2387a8 | -3.16817 | -53.91242 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57698e2b-f0ac-3bbe-ba48-56cd204268eb | -3.15395 | -53.9823 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 449f7f36-5b13-3d94-bd90-d1459d8e9568 | -3.09888 | -53.83341 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6903f055-ed4d-388f-9b5e-a7b92894dcc0 | -3.03634 | -53.79486 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 912b64a3-d07b-3ad0-9d08-e75ec49a4303 | -3.03579 | -53.79838 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c313ac8-3eb7-352c-95d1-3dd1857b96d6 | -3.03525 | -53.8019 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a87377cc-ae5f-3485-816b-412279d0342c | -3.03299 | -53.79433 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de4402c0-490a-3dc7-9ebd-ea3b490fc522 | -3.03245 | -53.79786 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 762b160a-89d2-3a63-826d-0bfd6e0e4f52 | -3.01436 | -53.87117 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b05ddb40-6ff1-3455-a6b0-00a0eed98f01 | -3.01382 | -53.8747 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a8ca3f8-68bd-3f60-abea-a6bbc4cc3265 | -3.0111 | -53.87434 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d733985e-8b0f-3fed-b8b8-b3a46d079317 | -2.99445 | -53.89342 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dac5510-6389-3c63-9978-d19bfc01f2b9 | -2.99166 | -53.8894 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22fdf025-74c2-3a43-8d31-d83699e93f0d | -2.98832 | -53.88889 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8de2c654-b631-3a26-9078-0c50971fc574 | -2.9745 | -53.91184 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 493b9f9f-fce7-3946-b7f6-c1b35b979598 | -2.97395 | -53.91536 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7de96c8c-b805-3038-bf34-edd413856db7 | -2.97117 | -53.91132 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56b9ea2c-f119-3418-9ba7-14c5bff8a54c | -2.97062 | -53.91484 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ef94b9d-96cb-344c-83d6-db5aeddd0bc1 | -2.96783 | -53.9108 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d6fdcc8-57ea-3135-8ffd-0905ee240531 | -2.96769 | -53.86767 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db139b3c-a1b0-3499-a4ad-91e7e000daa8 | -2.96728 | -53.91433 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44d94df0-9212-35a2-a2cb-1a7dddebc7d9 | -2.96449 | -53.91029 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b1924ae-29bf-3b9d-83e8-31e7e9578185 | -2.96395 | -53.91382 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f825c3e3-7ad1-353c-9ed3-dae42c3733ce | -2.96339 | -53.91737 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57f9cc7e-c88a-35ca-9a10-cb466112f667 | -2.96155 | -53.86311 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f5d4e0de-0421-31ee-beb8-26fb1dbc8eb3 | -2.96061 | -53.91331 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34784567-5743-311a-84d1-7a631dfbf21d | -2.96046 | -53.87016 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cacfac9-d450-3da2-9a05-09604511b3d5 | -2.95992 | -53.87367 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47e43389-4233-3e4c-8e4a-01f96af7e2ab | -2.95782 | -53.90927 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfec2133-a872-393a-bb6c-3f7eb69da1f5 | -2.94671 | -53.91484 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b408856-0f34-39fd-a774-7f1a98d41271 | -2.94562 | -53.92189 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff840510-bc11-3cb0-95c6-556ef8ccb0a2 | -2.94508 | -53.9254 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7f95884-57de-3e5d-96d0-e079df26745e | -2.9412 | -53.92839 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32655c8c-6672-339a-8d8f-d588e81df387 | -2.94066 | -53.9319 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b67c95-33ba-335c-afca-f0499388cd6a | -2.88339 | -53.97291 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34de2f0e-6046-3219-bed7-2b81347b2c9f | -2.87449 | -53.96437 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f70dbef-1687-3e98-8cdd-d0762be83c7d | -2.84458 | -53.98128 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e4d352-fbb6-3173-8eb3-9a36f454ef2c | -2.84125 | -53.98076 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08319706-47a0-3819-a4bc-1fd660aa0801 | -2.83962 | -53.99126 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44b21320-6586-330c-bc18-d2630c9f4d6a | -2.83792 | -53.98026 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 456460f8-5394-3349-a9e5-a206e55c5af8 | -2.83629 | -53.99075 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 161a6930-36ea-31ab-9a77-d2bf6eb96c44 | -2.80749 | -54.00065 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760cd5aa-98c5-33a4-a15c-97339e6c03ae | -2.80695 | -54.00414 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56455a45-f0f1-3754-88de-72a04266825e | -2.80417 | -54.00013 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7cd5d93-ae21-334e-a516-efe820e5538f | -2.79697 | -54.00261 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eda57e66-b3c3-32dd-bd2d-2d5cb8729de1 | -2.79364 | -54.00209 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 482e4c00-2117-311e-80eb-5bccfc084c1f | -2.78987 | -54.02654 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c127724a-c944-3404-8b56-d2d0a031596d | -2.78933 | -54.03004 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 490ec294-38cd-34d5-9d25-b87f8f6d1102 | -4.5095 | -55.46137 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e65b944d-e6f1-3ecd-940c-56fdad553324 | -4.50562 | -55.46064 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 53ba8136-6327-3c77-b24d-402da264a6b8 | -4.44873 | -55.39203 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b11b39a-3f7b-3e8f-af92-37eaa2f0d73d | -4.43116 | -55.39635 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae35be5a-a151-3d3f-8ec9-ad616bb87fbe | -4.42839 | -55.39241 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 336f7136-a9bf-3691-b9cb-b2ed1d404bb6 | -4.42563 | -55.38846 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07b36e87-9279-3d1c-883b-c6c936a8e1ba | -4.42509 | -55.3919 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 144e0ba6-876c-3218-807a-56b37c2fc4df | -4.42456 | -55.39533 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f9d9d26-f5f6-319f-ad57-ef4dccd54470 | -4.42402 | -55.39877 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 495de90b-0e7b-3e31-b991-1ef194f23e63 | -4.42179 | -55.39139 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8f7116d-0a3e-315b-9da8-a372e4ad7759 | -4.42126 | -55.39482 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 714f541c-bfdb-3d53-a34b-858cc821b424 | -4.42072 | -55.39827 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18032044-8f59-3538-8927-46fdceedb93c | -4.41466 | -55.3938 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0d6627d-fc8c-3f6a-9675-fb0d28994adc | -4.41412 | -55.39724 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03dc0973-5e71-3a71-8c84-fb9f09f3adbb | -4.3717 | -55.42585 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a574d957-46f3-3c05-abf6-e93840d5de82 | -4.34558 | -55.35496 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acc60d1d-d387-3d0c-b746-01c887061eec | -4.34228 | -55.35445 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| debea328-2ccb-3dd5-b8c8-d170c31ef884 | -4.33444 | -55.31807 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README83.md)
