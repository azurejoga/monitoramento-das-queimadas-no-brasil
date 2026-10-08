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

## Dados Diários - Página 224

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff5c06c-17ab-3046-8d86-3a030e23b4bd | -2.8434 | -57.4696 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 918ac606-dc6a-3ad9-a7e4-c9ab3e40a467 | -3.1633 | -54.7253 | 2026-10-08 15:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d290479f-c040-3f83-b7b7-377038c1840e | -1.3277 | -55.4327 | 2026-10-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 56fdb00b-9052-3cc9-a81c-d14323c2d657 | -2.8163 | -54.133 | 2026-10-08 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ad48707a-9032-3145-88c3-2e07d8556ae1 | -8.6107 | -67.0301 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 460.9 |
| b512e592-9240-3b7d-99fd-2d6db3e6e2d8 | -2.7613 | -54.074 | 2026-10-08 15:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 258a830c-d927-3195-8890-655525227477 | -8.6107 | -67.0116 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 9ee6983d-22d3-3575-b35a-b96eeb5a5bef | -13.1641 | -54.3178 | 2026-10-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 2460021b-ee53-35cf-bb3e-542a68f338d6 | -3.1133 | -59.1828 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 72a1cc07-0f03-3ab2-a72d-08422b12cd58 | -3.0765 | -59.2794 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5f85aae8-93f6-373f-85cb-a58e802933a6 | -11.2661 | -45.1859 | 2026-10-08 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 30dfb8f1-caa3-35f6-bc8e-fbf73c60f42b | -2.8347 | -54.1125 | 2026-10-08 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1c5439b1-6b67-34eb-9acb-0111837c084c | -1.5307 | -54.5159 | 2026-10-08 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3f75f21b-c67a-30c4-ad1f-b3aa3d66312e | -2.3863 | -57.2247 | 2026-10-08 15:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9c00ed75-aaf4-3419-8723-1d21a61d97d3 | -5.3462 | -56.0256 | 2026-10-08 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 86cac318-1c87-36f4-97c7-cd907c9a658b | -3.9483 | -56.0138 | 2026-10-08 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 0d9fc21f-99de-381c-bd08-4fae32627483 | -3.1697 | -58.6437 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 262.1 |
| 812989b1-29b2-3086-aea7-d89e65fde125 | -3.7346 | -59.4577 | 2026-10-08 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0d462dae-e37a-3ae9-9cb5-3346ce435b36 | -2.3115 | -57.9829 | 2026-10-08 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 7920e10a-5b28-3852-a82e-c155bb0e71ea | -1.8803 | -53.9701 | 2026-10-08 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 697f88a9-7187-32fc-bf7b-853805aa753d | -3.2554 | -54.6631 | 2026-10-08 15:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 43c6b013-e709-3ec3-a37c-3663b52b8f58 | -3.1697 | -58.6244 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 69322c03-a019-32b2-babf-bfa1dc640e86 | -3.8155 | -57.1751 | 2026-10-08 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| d5534d03-1d27-39d6-bd4b-34a8c3d969a9 | -7.2366 | -55.1606 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0ece5e24-800b-37d9-bc75-2bb1eabc9321 | -1.6213 | -55.1321 | 2026-10-08 15:30:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 666e51f3-3734-3f38-b0fc-e6f06a35c6b1 | -2.0447 | -54.3085 | 2026-10-08 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 65654d64-7279-3be0-81d5-98fba0ad4163 | -3.0982 | -58.0273 | 2026-10-08 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| cd7fcb57-bbf1-309c-863a-240757abd03b | -8.5428 | -54.5773 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a39e414d-7a5e-326f-9c97-8aca8a7fe14a | -11.6382 | -43.6166 | 2026-10-08 15:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| b9d7a411-d998-3fd8-8656-9ea62ef3a61c | 3.5448 | -51.2772 | 2026-10-08 15:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 85.0 |
| fe122b8a-afbc-321e-abcb-9257efc772ed | -10.9575 | -45.389 | 2026-10-08 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| fd4f3a9b-ac02-33fc-bac2-d7730b57516c | -6.1974 | -52.8295 | 2026-10-08 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ef53175e-09fb-3712-b886-de4315d7be44 | -1.383 | -55.1944 | 2026-10-08 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a722452c-b0ad-3f9a-bbb7-87d95084d21c | -2.572 | -56.1842 | 2026-10-08 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| be95febf-57a1-3731-a440-adab2212f64d | -2.6051 | -57.5905 | 2026-10-08 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 671188d2-1518-3e98-aace-7eba022dae6f | -2.6079 | -56.4782 | 2026-10-08 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| c81b0c40-b57d-359d-b715-49587b7acf31 | -3.2451 | -57.8693 | 2026-10-08 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3668b4b2-8668-3fcd-90e8-bcbefeb2cdce | -1.146 | -54.2199 | 2026-10-08 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 743e4e1c-6d65-3c11-ae6e-220b68c7ed96 | -9.4819 | -66.7836 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| d00bab1e-ded6-3d4b-85b0-125da46a3d58 | -3.8567 | -55.9769 | 2026-10-08 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ae468008-013e-3645-8724-5d6f54a054d1 | 1.6385 | -55.785 | 2026-10-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fd93e63d-e5e7-31fe-90ee-0ec038fcdb40 | -3.3175 | -58.1582 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3971833b-af3a-39e1-aa0e-50c87ee10cae | -3.1879 | -58.6433 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 397.8 |
| 38e6541a-fe3c-3206-935f-e67a75c999f0 | -2.4806 | -56.0875 | 2026-10-08 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 898665c0-34c0-3902-b098-9380dfd3707b | -3.3687 | -59.427 | 2026-10-08 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 939a18e6-bb17-30e0-9752-558c557626b8 | -1.8977 | -54.3909 | 2026-10-08 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| bdbb38bd-3721-30c1-814f-d835ddb10183 | -3.095 | -59.1832 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e23a3dfb-9c90-30a9-8b69-51c34800c4c8 | -14.3608 | -55.032 | 2026-10-08 15:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0b5584f2-8a68-3347-9442-5b1f6b4fa574 | -7.2371 | -55.1005 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| df6f40e0-c206-3bd7-b749-8ce1f9eb15df | -3.3358 | -58.1578 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cc74eb93-3c2d-3757-835d-8571f1b03320 | -6.6899 | -45.3746 | 2026-10-08 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| a316a1f8-4635-33d9-b9b5-6ec9d660388c | -2.2198 | -58.1196 | 2026-10-08 15:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e65e877e-49da-3f69-8758-d41c0b0ae0d6 | -2.8897 | -54.1514 | 2026-10-08 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9054c3e1-6b6e-3012-b1fa-594f0f557460 | -9.479 | -67.4897 | 2026-10-08 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2059e29b-76c4-361a-8f07-d8f11b1d845e | -7.2185 | -55.1016 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 3f22dbf3-ac56-3748-8752-2bf42429d911 | -3.1484 | -53.7225 | 2026-10-08 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4f8ff730-3a86-304e-b107-78beedbd8aac | -3.3912 | -58.0017 | 2026-10-08 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bd6b398c-0823-3d14-bd80-95e263d6f657 | -2.9707 | -57.7585 | 2026-10-08 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c7b0acf4-fa7c-36c1-bd48-af993b73cf18 | -9.1408 | -64.3836 | 2026-10-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f7dfaef1-388f-3bba-9de4-84c6944924d7 | -1.3264 | -56.4176 | 2026-10-08 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1e37bcd1-20b1-3ead-9c07-7119344a4851 | -3.8383 | -55.9774 | 2026-10-08 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d8033108-fdb3-3595-8ab6-7da51b2255e1 | -2.7332 | -57.6077 | 2026-10-08 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 13861022-606f-3749-907b-0964fa491ae8 | -6.737 | -55.0674 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 84e243ad-9b65-34d3-9b6a-37e0d4c69d20 | -7.1998 | -55.1226 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e3d975e6-e612-3a7e-a16e-0917a9dbc037 | -2.8531 | -54.1121 | 2026-10-08 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1080fe05-11ff-367d-8ec8-75ad178422f2 | -3.8566 | -55.9967 | 2026-10-08 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5ba2472d-2915-3660-a44a-685f30e1ffc1 | -7.2 | -55.1026 | 2026-10-08 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8875efcb-3625-3f3e-910d-e5bf13fd4d38 | 1.6568 | -55.8045 | 2026-10-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 89ac1ab1-591c-3160-af6c-612071878764 | -12.232 | -44.7194 | 2026-10-08 15:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 181.5 |
| ade5c459-f468-3379-9cdf-124105f914e7 | -1.3264 | -56.398 | 2026-10-08 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 52c66bcd-6c33-3c15-b670-da40f8174ed8 | -9.4751 | -64.3336 | 2026-10-08 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 680ebc87-ef55-3853-abc0-d76978c98709 | 1.6385 | -55.8047 | 2026-10-08 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e953f111-1e6b-338c-ab01-d8a64521c8a5 | -1.5123 | -54.5161 | 2026-10-08 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 32ecda5f-3e64-3a2e-94e9-01960c0a86b3 | -3.8338 | -57.1746 | 2026-10-08 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| d6c0144f-c5e2-3382-9fc5-af9151f71c48 | -3.6252 | -59.3259 | 2026-10-08 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 74089d2c-b1a7-30ef-866b-cd83dab3ae52 | -2.8938 | -59.2251 | 2026-10-08 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a8e6c273-e446-3a3b-9ddd-d056196d1bb7 | 2.764 | -60.0297 | 2026-10-08 15:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 5dc96356-c821-36dc-bc2f-be4dc6198048 | -8.6106 | -67.0486 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 365.8 |
| 55cf8adb-ef68-31af-9721-2a5eade11e32 | -13.1639 | -54.3385 | 2026-10-08 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 179.1 |
| b83664e2-d5be-3f16-a2b5-672deb0f7a90 | -9.2067 | -66.0842 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1c33747f-481e-3901-9908-5df95794dcee | -7.6033 | -55.7194 | 2026-10-08 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 93dd4726-a969-3ff0-92b9-921f6a703b63 | -9.5003 | -66.8017 | 2026-10-08 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 181.6 |
| c658cace-a859-3773-80d1-de3480352f0e | -20.24115 | -42.07214 | 2026-10-08 15:37:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6949d385-4be3-3864-a769-8fb35f2237af | -19.50434 | -41.60308 | 2026-10-08 15:37:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 99cfaff1-2f5f-3749-bd83-f36f70c38fcd | -18.9639 | -41.17595 | 2026-10-08 15:37:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 92697832-c250-3561-941a-1d735db90d30 | -19.35492 | -43.32051 | 2026-10-08 15:37:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 24fd6882-42ad-3782-b954-5bca1d3b5f94 | -19.76304 | -42.19519 | 2026-10-08 15:37:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 14f70a4c-6b95-3130-8784-25bc97f8164e | -18.98372 | -44.45728 | 2026-10-08 15:37:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2010ec01-755e-31f0-8565-91667a493f2c | -19.08164 | -40.08711 | 2026-10-08 15:37:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8122119a-e6ad-3d54-96d8-1fd3e6f560b2 | -19.60381 | -40.10244 | 2026-10-08 15:37:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 7ca59874-84fb-3431-9760-29bbf681ef5d | -18.54182 | -41.05867 | 2026-10-08 15:37:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9580b80a-701c-335f-8035-950ee291e486 | -19.63827 | -42.04978 | 2026-10-08 15:37:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a51dc961-9c9e-399b-a598-1b75336ffaad | -19.40833 | -40.214 | 2026-10-08 15:37:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 363ca343-4099-3e8a-88c5-8bf24c193768 | -20.26846 | -42.64939 | 2026-10-08 15:37:00 | NOAA-21 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5d3c9f5b-d69b-3305-a100-9c58a1d59448 | -18.9817 | -44.4557 | 2026-10-08 15:37:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fddaf126-f5b8-398d-92f8-73c22715e98d | -19.08412 | -40.08871 | 2026-10-08 15:37:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c6dd0106-1f85-3105-8cf9-586d6eb10a49 | -20.24218 | -42.07103 | 2026-10-08 15:37:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9a83a0ec-0f84-3284-a150-2fedea7810cc | -19.59835 | -40.10304 | 2026-10-08 15:37:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 6888beb4-a33b-3a82-a84f-55c5eedf9e28 | -12.02927 | -43.43977 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 52fbbb6e-460c-390a-abdc-80971f9f9edc | -12.08826 | -38.75666 | 2026-10-08 15:39:00 | NOAA-21 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |


[Clique aqui para ver as próximas entradas](README225.md)
