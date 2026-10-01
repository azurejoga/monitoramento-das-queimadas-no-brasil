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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2966607-48a2-39fd-a1b4-eb74a5370dfa | -13.34027 | -46.82222 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f3f3e2a-b776-3320-9eca-66f2294d94d7 | -11.43734 | -43.41778 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 464997b4-0746-3c95-b20e-1c0a610e9c92 | -13.36261 | -46.83335 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 089d1d60-1555-37fb-be54-046801d8d24e | -9.8029 | -44.81374 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50b8b080-f01e-3ed2-a271-0f06e826ba35 | -11.44742 | -43.429 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 79050feb-8883-3be5-add7-f8559885dc7b | -12.38456 | -54.09552 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 449e6e77-cdbc-3010-9d38-3a34f982a741 | -10.25437 | -49.67282 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef050b29-888e-3933-ac41-2eedd52f23fd | -8.79315 | -48.00496 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f615431-fa84-3725-8a8d-7f324000cb46 | -7.71902 | -49.54628 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa65f7c1-292f-3539-b6cb-71a998cb6941 | -7.72768 | -54.79704 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e6a0c31-04d2-334f-b7ff-825a60f4f72c | -11.26782 | -43.52341 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ab5950a-3247-39af-9409-107acd1b383e | -8.12983 | -43.53183 | 2026-10-01 04:34:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2dde67b-7b20-3667-ae44-f4318c3dd577 | -11.4481 | -43.42423 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5380972d-69e9-342c-9d3b-6ffab2eff566 | -8.00856 | -47.45175 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 443edac1-6ae4-3645-b318-24193d89450a | -7.60716 | -44.55489 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2cfaee2-a1f4-3110-8352-d53d3f249bd7 | -7.84821 | -45.82298 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e521917f-ba1e-3455-9acb-7ccf6aa96a19 | -9.80754 | -44.83037 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da9b0e8d-3138-3349-88c1-3f89390d5ea0 | -5.86688 | -57.7618 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a599170-4ee0-3646-a3ed-07b86f2c2a1f | -12.38967 | -54.09206 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e267d9-31f5-3830-9a25-52e306d3a814 | -11.12068 | -44.59721 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb62ad7-9da5-3203-9209-2d86ef47b102 | -14.73892 | -45.19737 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1ee1f6d-62df-3be8-a248-2fae29c1be80 | -11.2242 | -45.1855 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fc5fa08-7e65-37db-8f79-64ffcd64681f | -6.35103 | -55.33456 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d3c2b09-8a8b-3d16-b493-957c9a3c8a1c | -11.21566 | -45.14785 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d0bfaf0-58cd-33d6-98f9-e88bda01d804 | -11.26485 | -54.81446 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd9ecb7e-eeb1-36ef-9b20-fd685787a2dc | -6.72379 | -52.95729 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d4d88c-5c84-33f1-9ff9-b7cb8a691e31 | -10.83963 | -48.69425 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b42e05c-d58b-385e-a9da-18740db27441 | -11.45093 | -43.45859 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89c9ab5e-a460-3f47-9305-6ebdb0b82dd4 | -11.70318 | -43.45204 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fc7826e-2bec-3d5a-9b50-fc1f15e67e83 | -10.85357 | -48.69322 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8dcac57-2bf3-3fbf-816e-af13663a203f | -13.38024 | -46.82016 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 287def06-80dd-3558-b004-c2e9755bbf57 | -6.7041 | -55.05087 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aa756c0-ed8f-3667-8521-15dda75bb96a | -8.21173 | -45.49245 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8fd3e25-fe4b-3f3f-bf8f-042a0f4959f3 | -9.33756 | -57.17887 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87da55af-2218-3ee1-ac12-27ea8ea1aa6f | -7.81383 | -49.84971 | 2026-10-01 04:34:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d7e2107-e9a1-3c4e-b0c2-0e0f2d251289 | -10.53262 | -53.7183 | 2026-10-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec8a3f6c-9d16-37f1-97d7-67d03a37244b | -11.41062 | -43.41381 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c7bc595-f71d-3f5f-8e78-ca679961e4e7 | -10.53097 | -57.77338 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4f140fb-9a73-3dce-842a-4957f85a7ea9 | -8.01099 | -42.89123 | 2026-10-01 04:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3649144-835c-35ab-88e3-ad36ad178464 | -11.17386 | -45.11739 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73f3f903-f449-3b1e-b6fc-5dd0050541fe | -11.25578 | -43.52638 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2ec4818-c20c-3fe9-b2c1-c8d9e644d0a1 | -6.74168 | -55.59713 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45149260-de22-39c7-b203-80b53b54e824 | -8.32613 | -46.75791 | 2026-10-01 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 674d14ec-06c8-3159-be08-020c876c3b65 | -12.18704 | -48.43294 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9c834878-c7ef-3749-8683-8ccccecfcbb5 | -9.19612 | -45.73664 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 962a21c1-97b9-305d-9eae-b08ba9433013 | -12.56207 | -43.07251 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 656acf4a-b38a-3f2e-8968-39543461cb1b | -5.85299 | -57.76818 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3b582f0-0e0c-3f51-a7d8-9d4720e7b0b5 | -10.45697 | -46.76836 | 2026-10-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1e37c162-d763-3428-a98f-cd87c09454e9 | -8.62676 | -45.3253 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 547b565a-0934-3248-9253-168fc74064a9 | -7.54112 | -47.12266 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16e6fd91-9a27-3422-b075-1570ad47cef2 | -8.62733 | -45.32164 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2211608e-282c-32a5-87e7-14a039f97407 | -6.6782 | -58.87403 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ce2175c-69ef-3045-a59f-2daddab5e357 | -7.82043 | -45.82578 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c22d7a8-bc38-353f-9cb0-4b0a1c6a9a05 | -12.18707 | -47.38522 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b26dc298-c40f-342a-bdc2-c462a8d33838 | -9.2111 | -50.68649 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a329eef8-3066-3156-a23e-2aaf6f21b57a | -6.92272 | -59.28254 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57de7610-9fac-3932-8206-9d24b2de42ca | -5.85497 | -57.76225 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a919f466-11f8-3ec8-88b6-71b053ac7726 | -11.19172 | -45.18839 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9edd51ae-c338-36df-abd8-9d513ced9e64 | -8.20835 | -45.49197 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff1629b4-c995-3ec5-9156-fcda81655cbc | -8.00912 | -47.44826 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce88f0b6-f6d7-35f7-9d54-4c978bf99f14 | -10.71786 | -44.41547 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dcbce4e-10ba-358d-a7c8-567e0e774503 | -11.42521 | -43.42082 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48fd1047-ba40-3a35-a231-d27689fa8b98 | -14.36288 | -44.77534 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed509d79-4197-336b-88ba-a2d60d34f497 | -12.26179 | -53.99226 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afbf1760-0d8b-3f99-8f5e-6eaee01535e9 | -14.14585 | -46.24161 | 2026-10-01 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2192cd25-fa35-3c25-8750-31ec586437ac | -11.70156 | -43.45398 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8f26ad0-e4f0-38a2-8258-0adeaa3f7728 | -9.35092 | -57.16947 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dca681a-e0a3-3496-8536-1761a496aded | -9.7544 | -44.81906 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2815aa2-f42e-3182-926a-07e75639ac27 | -13.38155 | -44.0185 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7955700-a541-3546-8a07-bd8c9b589538 | -7.61061 | -44.55542 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914af1a9-0ad2-38fb-a7b6-7d38b8172bc9 | -7.59666 | -46.66582 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6d88449-e7b6-3b8f-99dc-6cef001f1050 | -11.17503 | -45.10951 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba068357-0929-3f35-a866-1af8cbaf64c0 | -7.1854 | -46.30222 | 2026-10-01 04:34:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f930afc5-0348-3df0-bb48-c39c677dee2a | -9.90208 | -50.15835 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e1b1205-7b7b-33e4-b78f-1adc7d534d51 | -6.1389 | -53.05773 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82f09eac-0506-3369-92f0-7f4c424c3ea0 | -11.40843 | -51.0226 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c52c5ac2-6493-3598-9cbb-4cc7f7b156c3 | -10.60612 | -48.05653 | 2026-10-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5407d955-ac03-3982-bc05-69f33f752169 | -7.49952 | -45.83693 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d66d3bd2-cbff-31f0-8e7e-ba21e6f271c6 | -12.7826 | -47.28821 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3182bcd-e524-3608-96fd-34db40561cb8 | -7.54749 | -55.02668 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04da7094-6234-3ddd-94a7-3c2ea094962b | -10.65765 | -50.75879 | 2026-10-01 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b98c709-b57e-3c9c-84d1-223ad7a76a8a | -6.50819 | -55.88569 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d829b21d-8685-342f-9452-b146299dcc22 | -11.65955 | -43.53777 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01840da4-68ad-3c04-b039-1947b272148b | -11.79118 | -50.4173 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c1bd5c4-4ebb-3926-8f3f-8e0eed6ff402 | -13.37802 | -46.83477 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1627a579-e062-33fa-8bc4-6f0e427d128d | -11.40432 | -43.48558 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6ef7b84-34b2-30b9-a07c-7da334e1be5f | -10.51128 | -50.84966 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d8d08e9-b7f0-3e63-ab6b-17c8fc809cf7 | -7.48109 | -45.77999 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7da3a6fa-ac4c-3d29-8e9b-8513d24f69e9 | -11.26851 | -43.51873 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa9b0b21-41c9-3d21-a13a-1c4554cd72dd | -13.0645 | -51.19088 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f79273f-4be8-3306-87e0-0ac4ac87ec26 | -9.79244 | -44.8121 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed6a2b7-915d-3203-af1c-48ac58869234 | -6.59083 | -52.12059 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62b1c2c6-4f0e-31d5-b536-da60698cd148 | -8.77488 | -47.84231 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 057d0f9f-3b8e-3d89-8342-f45211e48642 | -10.21396 | -45.31438 | 2026-10-01 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa86e010-6655-3f64-bb0c-5520631f99ff | -6.34062 | -55.33255 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa6f6e5b-1397-30e5-a817-f7de64d62111 | -7.48442 | -45.78052 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f59f445-08db-388e-9286-ba8173f88368 | -8.85289 | -49.70549 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20bb4b88-5adf-3f96-9e70-6a6b746a1c05 | -12.19038 | -47.38575 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c405e3b-a342-328f-8a0b-c23b78b5e88d | -9.86382 | -44.98899 | 2026-10-01 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e5dea9f-e0fb-3983-a2e1-53eb1c92c2bc | -10.84179 | -48.70213 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README66.md)
