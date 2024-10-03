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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fcb69b7-adcd-3268-a0ff-9c7641b46d8c | -8.17127 | -55.15993 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb3220f6-671d-3341-bbfe-feeaa7dbe9f8 | -8.17072 | -55.16296 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c2547dc-176c-31f6-9d4b-dbfdc9b04239 | -8.16703 | -55.16117 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecb80d68-acab-3bed-b275-4b0cc54cfeb0 | -9.57749 | -56.02333 | 2024-10-03 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 89498ce7-8ebc-37f8-94fd-045725a4a1b8 | -10.62729 | -55.88057 | 2024-10-03 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83ca6f65-a326-3fc6-bcc8-321275ff4146 | -10.62672 | -55.88366 | 2024-10-03 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eee1d38e-81bd-3a13-ae3f-bd7c709fd93f | -12.61606 | -56.48268 | 2024-10-03 04:27:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c041e42-1e18-3b9d-8c37-443909891143 | -12.61545 | -56.48581 | 2024-10-03 04:27:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 821a29bc-a2c8-3771-bea6-0f984c363e1d | -12.61035 | -56.48479 | 2024-10-03 04:27:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03bdf7a1-181d-3432-983e-2daaa6d0de22 | -11.99022 | -57.19559 | 2024-10-03 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2fbec42-ab27-3fb3-9da8-5706954971bf | -11.98952 | -57.1992 | 2024-10-03 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 566c0b51-6d09-3921-98b6-75ee2cb8329f | -11.98548 | -57.19104 | 2024-10-03 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0ab21f6-ee0c-36f2-af9c-820e0151d400 | -11.98479 | -57.19463 | 2024-10-03 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 36827ea3-42de-3517-b747-7c62378f1749 | -21.4415 | -44.5864 | 2024-10-03 04:27:03 | GOES-16 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| bc39659e-9734-385a-8a3b-8a20f077aac9 | -21.4623 | -44.5806 | 2024-10-03 04:27:03 | GOES-16 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.8 |
| 29e8d302-cdf3-3cb6-ae2e-868b7e021b2d | -17.85384 | -41.42458 | 2024-10-03 04:29:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fa73ae59-71ec-3cf9-9780-96476700c49a | -19.44111 | -41.37508 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e7f3f12b-6c67-38a8-a033-450186621139 | -19.4406 | -41.37972 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 62b278e5-3d7b-394c-a222-9cd8a9cdd486 | -19.42835 | -41.35864 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 7b9b8b6f-e42b-3609-b312-79f00d54de4b | -19.42775 | -41.36407 | 2024-10-03 04:29:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| fd3d0f1a-ba80-3b65-a772-463a729e2797 | -19.24759 | -40.63019 | 2024-10-03 04:29:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ae87adeb-bae8-3cb7-9a7e-92dcf48a3334 | -19.24727 | -40.63301 | 2024-10-03 04:29:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b7f7280e-426d-3534-9452-a3c244620cca | -19.24257 | -40.62945 | 2024-10-03 04:29:00 | NOAA-21 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef69eb0d-df8b-32d6-a6c4-9c331394e17c | -18.91265 | -41.27475 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 93f2fe27-aea6-313c-aea3-4af0452ae669 | -18.90096 | -41.20915 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| dda6e0d6-2a88-3239-b58f-beefafeb8a1b | -18.90029 | -41.21486 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| afb45e9a-a7e9-38b1-9c80-f2970cd0f9b2 | -18.90021 | -41.21114 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| 8f83027c-c3ff-3e31-a7f2-8b245c6fc1aa | -18.89614 | -41.20861 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f85d2bb5-35a1-3442-bc69-16c42cdcaf89 | -18.89538 | -41.2107 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e3317e4b-d579-360f-a1a2-c9c18a55ff67 | -18.89133 | -41.20799 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a196effd-e1d4-393a-b36e-d89df85b1840 | -18.89064 | -41.21389 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c4c68a85-8420-3de0-9225-982ee98313fb | -18.89057 | -41.21005 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 736104ad-3964-33a4-afd9-5ec0bcb0dff8 | -18.88999 | -41.21949 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 6d99c01a-a195-3875-b0d1-8cca980a998d | -18.88994 | -41.21582 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| f598d305-d4ea-3269-80c2-47951dd36e86 | -18.88933 | -41.22141 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0c7c696a-728a-34cb-af14-955aa647ebd4 | -18.88578 | -41.21373 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| d0ac87e3-4157-312d-9d46-f29283ce0f26 | -18.88512 | -41.21939 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 125d6acf-3c7b-33aa-992c-e97391749d0c | -18.88507 | -41.21581 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 122ae184-254f-3123-83f4-86ce9bf6aaac | -18.88452 | -41.22454 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 23e8a7fe-ff8b-36ed-aeee-5548e2267668 | -18.88447 | -41.22129 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 5b1bfaf5-51fe-3167-9e87-c5bba17c6e82 | -18.88211 | -41.24526 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8c5568ad-5d17-37e4-8959-fb7afe39adbd | -18.88163 | -41.24729 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 11c1de1c-f074-37ab-bb2f-cd1f7a896296 | -18.88143 | -41.25108 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 30e810dc-df0e-36fd-b58d-1ab5026cc976 | -18.88022 | -41.21961 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 40dd65a9-d226-3da5-b4a8-92d174dd3f1f | -18.88015 | -41.21626 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| dd20f07d-e1ca-33b9-91a9-47f95d9a93ea | -18.87959 | -41.22135 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 386f96ad-8c9d-34c9-bb9d-f18ec1eb7d7d | -18.87729 | -41.24482 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 528d27b2-e86b-3859-b50b-113980f24b12 | -18.87681 | -41.24683 | 2024-10-03 04:29:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 48775188-d728-3d3e-b42d-89815fa195a5 | -20.81739 | -41.6278 | 2024-10-03 04:29:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e3d56754-9e9c-3086-9346-f283e42bd730 | -20.81315 | -41.62208 | 2024-10-03 04:29:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e79f55f-ac5f-35ab-a080-2cf12fe0175c | -20.70361 | -41.78012 | 2024-10-03 04:29:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 48d5873b-d2dc-31a6-a231-5d1002cc0316 | -20.69049 | -41.98328 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 7f5d709a-29c0-3fbb-814a-49bcea805c7d | -20.68627 | -41.97864 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1a2dde27-baa7-3166-b41f-e598a7cd9ceb | -20.68578 | -41.98298 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f4d0bee5-26f3-3c80-834b-835646831f49 | -20.66929 | -42.00325 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 2f7efdbc-7b63-326c-b9d2-8a72803b6bc2 | -20.66882 | -42.00744 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2285670b-99ec-3639-a803-934ef68eb4a9 | -20.66458 | -42.00297 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 091eaa95-9d81-365a-9369-8d23003c345a | -20.66412 | -42.00708 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 72ff494c-eeb1-3d89-a1d0-24c1bd9a98b3 | -20.65993 | -42.00216 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ee1e34ce-df59-339b-bdca-912f4733e50c | -20.65946 | -42.0063 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a0db9d44-8cc2-3a21-91be-080df62c7629 | -20.65578 | -41.9969 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| f254b03a-8c43-3415-bfb5-7d2ad78efd84 | -20.65117 | -41.99568 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 557d6ef6-17bd-394a-ab75-6065c8bf2da1 | -20.65069 | -41.9999 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 7afb7317-6736-3f56-b82f-4a1dc458c4a9 | -20.63444 | -41.99274 | 2024-10-03 04:29:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7aeee450-b3c3-3f9a-980b-fa4f2d6195d6 | -20.4371 | -41.99672 | 2024-10-03 04:29:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a06d27f7-48df-358f-9913-7eb434c89ecc | -20.15409 | -41.86733 | 2024-10-03 04:29:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| feb9f44b-5009-341e-987a-0219c102513c | -20.15349 | -41.87265 | 2024-10-03 04:29:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3ea7edac-e12d-3c90-a00d-f3bc0901e333 | -19.88965 | -41.4058 | 2024-10-03 04:29:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0f63b52e-303f-348d-80f0-40d203398e65 | -19.74069 | -40.67477 | 2024-10-03 04:29:00 | NOAA-21 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6a190635-534e-3dd2-ad36-0f1cf45582b4 | -19.74034 | -40.67807 | 2024-10-03 04:29:00 | NOAA-21 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 22e25e57-ff35-38ed-8b08-ec57bbc5ade8 | -22.0784 | -42.09194 | 2024-10-03 04:29:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3aa3a3a9-5ae3-37c7-9e7f-2e110c6cfaf4 | -22.07788 | -42.09665 | 2024-10-03 04:29:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| b416cf79-73c4-3351-9860-517d1e842326 | -21.5713 | -41.23283 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b1ad0086-60cf-3468-ba91-ad34eb425a6f | -21.56044 | -41.23151 | 2024-10-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 29a474a9-be7f-3935-bdc1-4fc93f237aa5 | -21.56014 | -41.2436 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 63498863-fac7-3d6d-aaae-29b4f562d7f9 | -21.55914 | -41.24357 | 2024-10-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7057b69f-a0ed-351c-bb50-704cce440e26 | -21.55638 | -41.23094 | 2024-10-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 803b71fd-5432-3889-b2bf-c95d0d5c7fb7 | -21.55546 | -41.23095 | 2024-10-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9490bb5a-01b9-367c-9e6f-0f8b48a7351c | -21.51898 | -42.05746 | 2024-10-03 04:29:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7718f2ad-16c5-3379-ae38-4b1d27fd4a4c | -21.51852 | -42.06163 | 2024-10-03 04:29:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fda479e3-153a-3fcf-9939-1f2b97bdbc19 | -21.49134 | -42.1365 | 2024-10-03 04:29:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4bdd90e2-7004-32f3-91ef-8881fa635e2d | -21.48664 | -42.13597 | 2024-10-03 04:29:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c22c702a-0f00-3efd-9a0c-09f6411494f0 | -21.31858 | -41.40047 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 62eba9af-a18f-3cf1-b6e8-056eb270aac3 | -21.31616 | -41.3997 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2d5f31e4-ab27-32f4-b3bb-1325e951211b | -21.3156 | -41.40526 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1f9a5c36-8c9d-3d30-9206-d5e7e917f99f | -21.31375 | -41.39922 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 62e06aec-33b7-3d27-ba00-46c6417a1c1e | -21.31313 | -41.40493 | 2024-10-03 04:29:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 7be97243-ea6c-313d-9d62-ec14c5533b19 | -15.81089 | -42.48438 | 2024-10-03 04:29:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cba2d63-37ac-37dc-a49f-4bad6fc91855 | -15.81035 | -42.48848 | 2024-10-03 04:29:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc3a2154-6edb-3cfc-a04e-332f0880e510 | -16.33793 | -42.30021 | 2024-10-03 04:29:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2704ace7-a7a1-3c09-ab03-6fda93d1e324 | -16.33418 | -42.29513 | 2024-10-03 04:29:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| da6f7e26-1783-32f0-9272-751f91f61a46 | -16.33364 | -42.29944 | 2024-10-03 04:29:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 36af09f6-7a6a-3a67-9122-e5e0ccfb80db | -17.80266 | -42.90646 | 2024-10-03 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35293c9f-d25a-3a8d-b131-8b395692afc2 | -17.79844 | -42.90579 | 2024-10-03 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d54f3ce6-ce05-3218-9d83-e7001ebc5e22 | -17.32885 | -42.50232 | 2024-10-03 04:29:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| abf0af40-0a88-33f6-8784-37060134670d | -17.32829 | -42.50665 | 2024-10-03 04:29:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25056027-3b60-3314-a8ea-8c914d54a637 | -17.32398 | -42.50606 | 2024-10-03 04:29:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03658ee4-c579-305c-b9cb-c30a8a1c0afa | -17.85298 | -42.25306 | 2024-10-03 04:29:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 993c9c70-45d9-3d5d-a9a9-c63a40892198 | -19.50858 | -42.32842 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f4431014-7158-39fd-8181-bafd159a0bb6 | -19.50698 | -42.32139 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |


[Clique aqui para ver as próximas entradas](README100.md)
