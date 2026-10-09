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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf995790-0002-3a89-b648-e13fdbf7ed4c | -3.4327 | -54.535999 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f7d3d77-a8d0-3b12-bc04-18b2f48058aa | -3.521 | -59.541599 | 2026-10-09 00:06:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd201fed-210f-39cb-a9e3-b20e826aee38 | 0.7749 | -51.972599 | 2026-10-09 00:06:00 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e9674505-ee42-3004-8552-9c35743e29cc | -6.1022 | -55.704899 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3d5fe6-b7f2-39fe-8e30-2801586b9828 | -5.6083 | -44.841 | 2026-10-09 00:06:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f8acde8-4173-301c-b03e-d5e1be3667ba | -13.8853 | -43.816299 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d661bc3-c3d4-3435-837d-4a304ac26e94 | -12.0107 | -43.4981 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8bc34b71-d77f-31d7-9f0c-ba696c6f441d | -3.0964 | -53.7607 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de3c158-b416-3774-8b1a-10892dfd420a | -6.8516 | -48.772499 | 2026-10-09 00:06:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d4a6e2dc-dd91-360b-ae94-423072dfcb5e | -2.494 | -56.172901 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e229ee1-9af2-332e-99df-3ac3477eb184 | -3.0749 | -54.2644 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b303df4-2e7d-354f-9b94-584e4fe639e3 | -7.0998 | -42.5228 | 2026-10-09 00:06:00 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fc4e48cc-016a-393e-a963-4f222a3dc03b | -12.0212 | -43.455502 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c512f4d-a9cb-36fa-8160-84aeb4fc6424 | -6.1119 | -55.702801 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1348966-fbfb-34a2-a205-ec3ad8f1af11 | -6.863 | -48.7771 | 2026-10-09 00:06:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6d228eb2-cda2-3ff9-947e-a02d969f3382 | -2.4881 | -56.054199 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b669ba74-7e81-3de9-9b74-aba597421565 | -21.200199 | -48.268398 | 2026-10-09 00:06:00 | METOP-B | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c04e0c75-af20-3f16-84e6-821fbac748e3 | 1.6995 | -55.603001 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df0b6aa-261c-394e-87f7-c61f0603fe0b | -7.4151 | -44.761299 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a9388791-32d0-3126-bfc0-b23f91a630c7 | -4.2975 | -48.602001 | 2026-10-09 00:06:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ddf995-1f6b-3f41-a6fa-f1ea3a7aceee | -1.9913 | -56.948502 | 2026-10-09 00:06:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1c32ed-7a84-3ce7-935b-abcea6f86d39 | -2.9857 | -48.909901 | 2026-10-09 00:06:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07edf9c4-bf0f-31bc-8aa6-5b6858d973c1 | -13.2001 | -54.347801 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8de18f-02df-38fc-9e1f-e13d86b3f351 | -6.7282 | -55.1478 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e83f49-47d2-3057-9a64-14c76c72fad1 | -2.9934 | -54.128899 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349f26fe-1fc6-3756-ab74-d10088e65cfe | -14.4 | -43.806702 | 2026-10-09 00:06:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28612c3f-0037-3387-a1cd-4e5a3af5be42 | -11.4679 | -43.389099 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 349d71de-b6b3-3575-8fd6-dfd5d4a5c554 | -16.7561 | -45.2328 | 2026-10-09 00:06:00 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0a8ced0-8b09-3240-8900-c175d0d15ea2 | -3.2132 | -54.286201 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0fe549-4798-3954-8fd3-539d3acb6564 | -4.6673 | -48.959599 | 2026-10-09 00:06:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8286d42-82ac-30dd-aad6-88c80ad3b18f | -12.5395 | -46.521198 | 2026-10-09 00:06:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44adb0d2-68e0-3f37-999b-635dbce22fb6 | -6.9827 | -47.666901 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0cf0542-2861-30d4-8dc1-f61300c76d41 | -4.6337 | -50.9645 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6c678e-25d7-30a7-89b9-dfe2d7a0e454 | -2.9543 | -54.137402 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0eb195b-d261-335f-ac24-72029d4575a5 | -5.955 | -46.378799 | 2026-10-09 00:06:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba11a15-0d52-3784-a7b6-951d5cd31a36 | -3.0241 | -54.081799 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84840b97-2a45-30a7-9fff-b9b74bcc6186 | -9.6077 | -42.146702 | 2026-10-09 00:06:00 | METOP-B | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e9e1d604-4abe-3a6b-9481-88ee21799c91 | -9.7328 | -46.970798 | 2026-10-09 00:06:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a50a309-e886-3184-8dc9-2175eb943833 | -3.0037 | -53.897701 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7771e7c-7b10-35bf-a4e0-6c783eaf6eed | -1.0015 | -47.662399 | 2026-10-09 00:06:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f9d895-a2a8-3076-985c-6ea17a82a211 | -3.2335 | -54.655602 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a92fc33b-8bee-38db-a7a7-f8a6ab8ecd9e | -5.4127 | -44.621799 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb58a144-14af-398c-acb1-0d528fef70c6 | -12.3164 | -47.085701 | 2026-10-09 00:06:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61391be2-2956-3e1c-a2d4-b69c1ff2523b | -3.8963 | -58.934299 | 2026-10-09 00:06:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15e2c1e5-b9e6-37b1-8283-8d3e9edf8fc4 | -4.2991 | -48.608898 | 2026-10-09 00:06:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50c1c95-987d-357d-85da-f7ce341dcaa0 | -13.1656 | -46.873798 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b531c5f-00c4-3950-b135-b7d451916c9d | -2.9304 | -54.122501 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a629fd6-822d-347b-894e-b787b1c509cc | -15.47 | -44.2239 | 2026-10-09 00:06:00 | METOP-B | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08409f33-f2e5-35f9-a952-1d657ff965f6 | -11.6328 | -43.690102 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9daa3230-838f-38fd-873f-cb2abbdaec1b | -11.2742 | -45.1936 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d762d46-1d39-3444-ac3f-fa3cde65645b | -6.4421 | -55.0508 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa153cc3-d218-3bb8-a184-b90f556212f1 | -8.3422 | -49.124802 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20423b10-d267-3f25-936f-64240203220e | -5.7155 | -53.4893 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f5f2e2-b7e2-3414-9448-2ef65f4d9990 | -10.7568 | -46.6208 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3ea7d5-7d95-3378-8cc6-b73cdc20a0ce | -3.308 | -53.695301 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba6c4c11-dcfc-3c4c-84b6-a1878e58cfec | -11.8305 | -43.522598 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d718549a-c358-356c-8853-b7d227e640ad | -16.121901 | -43.741299 | 2026-10-09 00:06:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f21b027-a9c3-34d8-8f51-d4a239940790 | -9.8674 | -47.473 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a707fa9-bbf3-3b6a-985a-09bf49150a92 | -3.0058 | -53.907001 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5d4c7df-8f51-3370-a94b-6088435bf2e1 | -3.2046 | -50.563301 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e1de050-3543-3874-8910-a3b16074f273 | -15.3326 | -42.7733 | 2026-10-09 00:06:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0762a0b6-c12f-3bb5-a930-1a9743b18a8d | -2.3226 | -48.486301 | 2026-10-09 00:06:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0bdb9f2-0b3e-3d4b-9b63-f4ee508c6052 | -11.24 | -44.870201 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 910a6ba0-b3b1-376a-ba13-7343a535561b | -6.8614 | -48.770302 | 2026-10-09 00:06:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 189f0718-8d39-34e4-b2a1-a693903585ad | -4.6557 | -49.227699 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01017359-157d-3bf9-8614-2974c7576030 | -3.5971 | -54.6763 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71acc512-1ae0-3cc0-a9b4-93844e31351f | -12.028 | -43.483799 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce170b16-397a-314b-96e0-2fb99faad881 | -2.3918 | -51.301399 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bc6e955-c11d-36da-b657-38e9a571ba6f | -3.8907 | -55.8713 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbcfdb5-7f5b-34a7-b312-4796faa9ba86 | -3.8618 | -55.9725 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 554f578a-a8f9-3601-84f5-02c58bf2c7a4 | -4.6657 | -48.952801 | 2026-10-09 00:06:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a000b4e4-a143-3a91-99e3-d72f080bcaf6 | -5.6973 | -53.452999 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f71cb6e5-9ecc-382e-bc70-451bbf0064a8 | -9.8576 | -47.4753 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7abb1eac-9727-397a-b108-99dc5316a0c7 | -3.598 | -54.587601 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e167d6ed-c6b1-3850-beb6-7f1bab5443a1 | -7.5388 | -47.120701 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6671185-2fd6-3ac0-828e-26595349030e | -12.0265 | -43.4342 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10d7e38a-5d26-332a-9930-0ffecc10aed9 | -9.8356 | -44.7827 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfd93427-ee06-333d-9126-18b4cb4fa1f3 | -7.2386 | -55.1479 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25797d47-f78f-35da-b96f-c8775919f8c0 | -5.3717 | -48.974499 | 2026-10-09 00:06:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a540aef-517d-3387-948c-1abb5485698e | -11.2055 | -49.415001 | 2026-10-09 00:06:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bea94969-88e2-3c54-b338-0906bbb79257 | -6.4296 | -45.9328 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f3d2cf5-3aeb-3f73-bc45-98148c546417 | -8.9067 | -45.224998 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6698df70-420a-3962-8718-ddbc456070c7 | -3.0011 | -54.1171 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c644ad9c-c817-3d3c-b140-09fa56796c26 | -4.3277 | -44.652699 | 2026-10-09 00:06:00 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdfe4884-d3cf-3ad0-8c64-0b1fa4de58ed | -3.5458 | -54.676201 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 888a6449-3a0d-3239-b24f-ca4c39b6c5e7 | -5.8603 | -53.448002 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47135b96-bc5d-338f-8233-16b516405c6d | -6.9843 | -47.674 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0f071ba-df1b-399d-ba41-f95dd6c5fa30 | -10.8435 | -48.147301 | 2026-10-09 00:06:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efc8c0be-d8ee-3512-b8ec-fd9cfe0db290 | -3.3688 | -50.468899 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cac7bbe-ad5a-3a91-9f18-c5b16d3f0d25 | -2.501 | -56.158001 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f03cce5b-fade-39c1-af4c-be570f8fc583 | -2.516 | -45.410999 | 2026-10-09 00:06:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b373f8d-e277-39b6-ac3f-af60d411e86f | -1.5342 | -54.5396 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e4de3b-b4a3-303f-86de-2191740f80d8 | -2.9314 | -54.172798 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1c4bec-c2cd-322f-9c10-9a347928f4fe | -18.622499 | -46.441898 | 2026-10-09 00:06:00 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b5ce539-38d3-3c9a-bbf2-9f9e916c0516 | -3.5751 | -54.669899 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc14720-e558-3f33-8f71-3c5e95e2719d | -6.3731 | -56.210899 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8464671-0b0d-3494-8937-e5f2f8681776 | -3.0542 | -54.2174 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb4b673b-bcc6-3cfa-a00c-561018f20c00 | -9.7905 | -44.766399 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 77cd0a70-bfe2-39f5-94e6-f069dc0ed8e1 | -6.0381 | -44.0369 | 2026-10-09 00:06:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb865718-efdb-3603-888a-e7462ba26b7e | -9.0302 | -44.3881 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
