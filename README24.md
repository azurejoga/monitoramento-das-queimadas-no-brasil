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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 415ed83b-f6e3-3a49-b755-5fe8d4e314f3 | -5.314 | -46.49262 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e24b0e9-9594-367e-97b1-6af202a8e476 | -1.65286 | -45.89727 | 2024-12-17 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45570c40-e0af-3db3-aa83-d04aa80dec9a | -3.85602 | -49.15174 | 2024-12-17 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 199097ec-4ff4-3cd9-879f-4a28303739f4 | -5.09245 | -43.90318 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 326f74c1-3615-3b0e-82c8-3cfe8a635b76 | -3.334 | -54.08163 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c841ceae-87a1-30e5-9bce-4e2cac7f918e | -3.33359 | -53.85898 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3989531-92af-37e5-8493-529ecc3c417a | -3.15656 | -45.97236 | 2024-12-17 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33dba07f-2b47-3596-b770-2cfc2bc7be71 | -4.48301 | -48.11792 | 2024-12-17 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a54d805f-96a4-3ec3-ad96-ba0273f57c23 | -2.05024 | -46.66014 | 2024-12-17 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fe9b8e1-5c49-3cec-85ac-79afedb35324 | -4.25172 | -45.9975 | 2024-12-17 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f522300e-1cb3-3111-a2a9-dd4403e0095c | -5.09694 | -43.90085 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4af77b16-1618-3b6c-af0c-ec878c44fe8d | -3.59053 | -52.42801 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e052c126-41bb-3025-9174-43540fe68951 | -5.29598 | -44.93882 | 2024-12-17 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab91c8bf-597a-3077-bf47-9d499ee6e23c | -3.87282 | -47.03108 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3a64fa92-6229-3126-af60-dc954b9c65ca | -3.30726 | -53.36642 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 515cfe5d-5be4-3f5f-858d-d9557c49069c | -3.18443 | -46.68861 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3523d3e3-7b53-308e-9dc2-983f54fc8769 | -3.01942 | -48.02761 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c42ea8-a2fd-3989-b182-ccaaed9cc70b | -5.10021 | -43.91084 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e668ff01-86cf-3da1-85f8-b12cfac6edef | -4.02144 | -46.80627 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18b2eca4-6da0-382d-b72f-43f704fe1395 | -3.95575 | -47.05714 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c3e35f5-cea3-3b5d-98cf-fc7a217f86bf | -1.37994 | -53.47755 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5cdeb93-39a7-33bd-8113-39dccdf9533c | -5.3649 | -44.04919 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e0fc620-df93-32dc-800a-3385a54c6a54 | -2.51324 | -49.10257 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51031c43-ed12-39f4-8a20-b7007ac2425e | -6.16347 | -44.42516 | 2024-12-17 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05f80217-d659-3975-bd38-c1deb28318b1 | -4.37962 | -46.55217 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7e86f0b-053a-3e61-99c2-9df374bec6af | -0.62646 | -51.79247 | 2024-12-17 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eae1558e-912a-3e8c-87f0-106726c267a7 | -3.16282 | -45.98331 | 2024-12-17 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 828cf13c-cf5c-35e0-ad92-792ac93897e2 | -3.15564 | -53.17714 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981a36b4-cb0e-3a8e-8faf-b3d773d88359 | -3.99563 | -46.89817 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f4011c-24c8-31ed-b91a-dd06449519c2 | -4.6808 | -44.03809 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f4ab261-120f-3787-9e11-88514d49b9bc | -4.79012 | -46.39333 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4c16bf4e-ea48-3f4e-81b3-b8f8637b576b | -3.77091 | -47.16711 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ee8a92-a750-3ce0-b1ea-c5321af45ec7 | -3.43505 | -53.98365 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8c95580-73ba-3b9f-9817-692f16878e76 | -4.02512 | -47.03949 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a040bbe7-524f-3e2d-9939-042e694fe5ec | -2.99998 | -47.73485 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6514bbc5-4a38-30e5-9816-d122ecd7046b | -2.03383 | -48.57544 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2043d1bf-8c55-36af-9a44-aac4636957ac | -3.1299 | -46.61338 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6240e6a0-9355-36c9-ace5-958f46e121f0 | -4.08676 | -46.73585 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 637a9961-7fcb-3448-9aec-31c888bea537 | -3.01245 | -48.02655 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53508116-6d6f-3aa1-8fd5-54288cd03e1d | -3.67136 | -43.57239 | 2024-12-17 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488e0f4b-8744-3492-b09c-b09b47c660cd | -5.09034 | -43.91719 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 62c28eb8-032e-3b1c-beeb-da4ddc614a47 | -3.50427 | -53.95452 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d35fda2-6c03-332e-9275-b79df914183f | -2.6962 | -46.60041 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3365c494-8b96-3ec9-9e8a-4879e77ada48 | -5.2078 | -44.56211 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d629a67-579c-366d-8a11-ffc3de11f7ae | -0.6299 | -51.79301 | 2024-12-17 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2c94b44-d0da-3cc8-a94f-37c6d4ef0173 | -1.81764 | -45.63599 | 2024-12-17 04:44:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f3c66cd-b348-3c88-a3bf-83f44f680c4f | -3.94864 | -46.93114 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49a061f6-d084-398d-a341-1a8a3abb168a | -2.17894 | -53.74694 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0cbfc21-8488-3e21-b0b0-8cd976108abe | -4.07185 | -47.10414 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1031a5d6-7cf5-3946-931e-b8036e0e79ec | -3.92565 | -46.9323 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ef6d440-a775-31d0-8d7b-9ddba90b44fc | -3.23198 | -52.83721 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3946d083-8afb-3809-84ac-569e57a451ae | -1.69672 | -45.77528 | 2024-12-17 04:44:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb9a806e-f82a-3ebf-b87f-fff94868cc66 | -1.52251 | -46.01285 | 2024-12-17 04:44:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06e0410c-10ba-3ee6-ac27-c9ce106dc539 | -1.83664 | -54.09983 | 2024-12-17 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59069b61-60a7-3b86-b678-671a48207765 | -4.04765 | -47.01606 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea79545-f766-381d-8f41-f5c11833fea4 | -3.93604 | -46.88897 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12951e2f-f113-3fb4-b690-cc5be1a3acfe | -4.17316 | -46.72386 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9566616d-6853-3784-af53-e057c1f8c0ad | -3.50357 | -53.9589 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7587003-a768-3313-979e-f01e41e9c994 | -4.06931 | -46.72392 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a230fe25-840e-309e-aa8a-02e64f2ec31a | -2.84102 | -46.76736 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4ae285-d4f9-35ac-85b1-17c06de1e0cd | -3.78304 | -47.11203 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 496a95e5-34fc-3513-a22f-812fa02610cb | -4.36875 | -44.5783 | 2024-12-17 04:44:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34bb17f9-59a0-38a3-b46b-46f4d656ebe9 | -3.04586 | -47.97266 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79c7ef81-69b4-3ae8-a2b8-e17033441077 | -2.87522 | -45.24415 | 2024-12-17 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2da270c-a02f-396f-a08a-164b329c7ae4 | -0.85326 | -47.55915 | 2024-12-17 04:44:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b810874d-c0cb-3dbd-8151-c63f6fac18d8 | -3.50197 | -53.94525 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5258c1de-e237-38de-9afa-3398baa159c8 | -4.07239 | -46.72897 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba20a1c5-049a-35e3-9a40-3a6fc1e9a467 | -4.02104 | -46.891 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5117e13-984d-39f3-877a-c20493239a78 | -4.37866 | -46.54517 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3393dc2-8821-3418-96f0-ae00d1f96222 | -1.78714 | -52.02613 | 2024-12-17 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e25e43b6-e881-3194-9588-5517a4b0e0dc | -2.93379 | -52.7167 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65753dc6-b2dc-3aaa-a8fd-1d27e6931057 | -5.10169 | -43.90432 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6cc05f1c-1c19-37f7-88d2-493335050d5b | -5.3055 | -46.49636 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d39ae534-f723-3dcd-9f66-f5a2bcd9b41d | -4.01335 | -47.04226 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff2c9f19-0607-3610-b8fb-ca25007f8b1a | -3.95675 | -46.92789 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2dafd11-1778-3471-bbe8-c3ee904ee27d | -1.37325 | -53.47199 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84a1ea46-233b-30c2-a684-81a7d413617a | -3.85264 | -49.15123 | 2024-12-17 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b26b823-5235-399e-a851-ae8a2d6f5a8e | -2.74275 | -54.08142 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25a149fb-a9dc-3507-abcf-8c7f19fdcd9e | -5.21288 | -44.56046 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d871ea88-bb7a-324c-bf37-b71e2bc7e6f5 | -3.79622 | -46.8402 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a344ee6b-1e9f-33d4-8096-d4c651d48ddb | -4.62213 | -46.31593 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7470fa63-ebab-37ab-8da8-b719170d794c | -2.87874 | -45.24833 | 2024-12-17 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ef3d540-1ac5-3bed-884d-8787f0ac0ee5 | -3.19098 | -52.89061 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55b1bd97-6b03-33e3-bd87-8dc2e806642f | -4.10095 | -46.66829 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ce8f80a-aa9f-3bcc-82b4-b727b260c759 | -4.67107 | -44.0413 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f2c48da-80c5-327c-ace0-3ddf2d39faa8 | -3.02833 | -47.83107 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f63a1ee0-ea5d-3c3e-bda4-a25e1772ab85 | -4.057 | -46.9054 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e8f234-6381-34f8-8c2f-55ee1022deb6 | -4.24461 | -45.99125 | 2024-12-17 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 292f160b-d2bc-3967-8664-df633c46a19c | -5.20784 | -44.56399 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 228d35b0-b316-3eff-ae3a-f1b1379b2f73 | -4.65564 | -44.33346 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baa9a642-0435-3e26-959d-ba61e43d738a | -5.08637 | -43.90905 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c08b74d2-3555-3766-ad5e-a223ff9dca54 | -7.15198 | -46.69546 | 2024-12-17 04:46:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0483d22-935e-3f4f-8d73-c1efef673902 | -6.92449 | -43.50338 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 01e5f066-e4a2-3670-914a-26a1266ab774 | -6.9207 | -43.53014 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcd69fe1-cea0-32d6-a0c4-2831cc8b2bb6 | -6.96663 | -42.8339 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2918d890-6af7-3328-9cc0-85375a3fe9ec | -6.95895 | -42.82932 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51567af5-6bbb-3145-8919-90fae53bab8e | -6.96194 | -42.8302 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 92d9ec62-73ae-3e81-8c6f-9e8506f474f3 | -6.64098 | -47.34859 | 2024-12-17 04:46:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1690a532-3c8f-3103-9ab9-1ea8e5c21c2f | -6.96363 | -42.833 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23651222-b9de-363f-b732-3b20c1a108a1 | -9.2295 | -47.56723 | 2024-12-17 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
