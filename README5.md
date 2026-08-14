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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a79fa9a-c42e-3390-9629-ad7f85950e41 | -4.5057 | -42.5325 | 2026-08-14 00:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 413.1 |
| 36fa60ff-61fa-3c8c-aa1e-20de2a1d4342 | -4.4868 | -42.5572 | 2026-08-14 00:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 160.8 |
| e562e612-6466-32f8-80ca-526c5ee1af91 | -13.2415 | -54.2476 | 2026-08-14 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 7bcb7647-6bbe-36bd-8f2a-c3fcf97bf030 | -6.1489 | -47.2431 | 2026-08-14 00:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2aebd55f-36cc-344f-a4c2-57d3a128b001 | -6.6195 | -59.0416 | 2026-08-14 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 9fb373c6-2063-3553-a700-77bc8cb71bed | -6.9145 | -43.6351 | 2026-08-14 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3d7faa32-57a8-3518-ba01-92ef5132eb48 | -4.5055 | -42.5561 | 2026-08-14 00:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 411.4 |
| 871537da-7fb3-3aa9-98f0-bfbfdf6482ba | -15.0924 | -48.649 | 2026-08-14 00:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 2a6fbe67-414d-3fc3-bb94-bd93201682c8 | -21.8843 | -55.379 | 2026-08-14 00:40:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 71.2 |
| da7d28fa-dd81-3e54-bae0-1981f24aeda9 | -7.7123 | -46.2307 | 2026-08-14 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| b9df2751-856d-3aa1-8b9c-0ecd89c75e3f | -16.9191 | -54.1481 | 2026-08-14 00:50:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 23bfae8a-881f-3445-9588-d3750a1316ac | -21.9054 | -55.3538 | 2026-08-14 00:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f055d120-0ecc-3a57-b2b4-1607b53d2824 | -13.2415 | -54.2476 | 2026-08-14 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f32466cb-df52-3ee1-a4ce-93078e6e8780 | -4.5242 | -42.5549 | 2026-08-14 00:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| e05a9074-c23f-35cf-bf0b-e2133a067f7b | -11.4885 | -54.6273 | 2026-08-14 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 1b7c31a5-81cc-307b-8129-59563b83b36d | -4.5244 | -42.5313 | 2026-08-14 00:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 281083ae-13df-3cbc-8f16-beae5df3fe40 | -15.1559 | -41.5566 | 2026-08-14 00:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 133.4 |
| ba8ba63a-1e74-3b48-a7fb-56857d4aefa7 | -6.9145 | -43.6351 | 2026-08-14 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ac14f50d-5269-31ce-b92c-1a50cc017f91 | -21.8843 | -55.379 | 2026-08-14 00:50:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7a7a3b0e-43dc-3a2c-a308-903229e202c4 | -11.4887 | -54.6068 | 2026-08-14 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9689285c-ea66-34cb-b3ec-bec4353d3a5d | -11.5074 | -54.6256 | 2026-08-14 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| aa2d4884-3c86-3630-8fce-54c4433b48e4 | -4.4868 | -42.5572 | 2026-08-14 00:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 0a95b52f-ea9a-3ff3-9bbd-067d590e2ff6 | -15.1688 | -52.8241 | 2026-08-14 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2df7f70d-0669-3f91-9603-b1e0ad5e81f4 | -15.1362 | -41.561 | 2026-08-14 00:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 126.7 |
| 2c54f7f5-28c8-33b1-a794-07003d52f8f9 | -6.6379 | -59.0409 | 2026-08-14 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c965d17e-17b4-3fa9-8cc8-68ee31d922d2 | -6.6194 | -59.0609 | 2026-08-14 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 75ab3c1d-cff6-396f-a428-657dd3127ac5 | -4.4869 | -42.5336 | 2026-08-14 00:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 9a508610-4d8c-3d24-9dfe-c46c32856b6b | -21.9049 | -55.3755 | 2026-08-14 00:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 558768b0-9df8-394b-bc13-6c615509c302 | -4.5057 | -42.5325 | 2026-08-14 00:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 305.1 |
| 03d26d2a-0f92-3752-a486-aa48cc55dcf2 | -14.4734 | -45.6914 | 2026-08-14 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b5a897e3-9d6e-3a7a-9d20-938af7d472e6 | -11.5076 | -54.6051 | 2026-08-14 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e8223ab7-99c1-3b30-bdc8-9a3f8251a42a | -4.5055 | -42.5561 | 2026-08-14 00:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 366.1 |
| 70353ceb-f559-3c83-892a-6168b5b0729b | -6.6195 | -59.0416 | 2026-08-14 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 0b4a7d1d-c5d2-38de-b72f-ca1edd9b9dd4 | -13.2415 | -54.2476 | 2026-08-14 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 97a7d93e-538b-37a5-a2c8-8115530ee95f | -21.9049 | -55.3755 | 2026-08-14 01:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7bc75c09-a892-37ac-be95-ab0b4d405291 | -6.9145 | -43.6351 | 2026-08-14 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2f4395ff-863e-37b1-9212-bf87caece835 | -15.1362 | -41.561 | 2026-08-14 01:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 158.4 |
| bc37658c-51e4-302e-ad3e-edcc58c17520 | -13.2413 | -54.2683 | 2026-08-14 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| a4c1547d-eee3-39f8-b2b5-411873530c8e | -11.4885 | -54.6273 | 2026-08-14 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| a752322a-603a-31e3-a29a-effb7a55fde6 | -16.9195 | -54.127 | 2026-08-14 01:00:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3c2c64fb-3b5c-3c53-831d-22f5e060dc21 | -4.5057 | -42.5325 | 2026-08-14 01:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 272.9 |
| c82bb07d-0483-3b2e-a0c4-a2a49c4ff140 | -15.1565 | -41.5316 | 2026-08-14 01:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 2f148d5a-af8e-3596-9c93-7a6fcb70348f | -4.5055 | -42.5561 | 2026-08-14 01:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 277.4 |
| 99e1cc9e-1f5c-3607-b6ca-540cbe17ce4c | -14.4734 | -45.6914 | 2026-08-14 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c1cbfa73-a313-3dd4-9b51-b67651865861 | -16.9191 | -54.1481 | 2026-08-14 01:00:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| dfe6956b-2598-3bb4-88ae-ec0cdc1178ba | -11.5076 | -54.6051 | 2026-08-14 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6644a79e-b663-38f5-b0a6-6b698068b31b | -15.1882 | -52.8215 | 2026-08-14 01:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 43c93927-29ef-3eec-bc78-c0e29932fc27 | -4.4868 | -42.5572 | 2026-08-14 01:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| f0fb560c-5cbd-3ff4-81a7-187c32bfe439 | -15.1368 | -41.536 | 2026-08-14 01:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 49.0 |
| e8083195-601e-300e-a554-e8f1ef7f21d7 | -9.9894 | -53.9608 | 2026-08-14 01:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 037f56f9-154a-3b47-9d6a-5a1c03dd2e71 | -15.1559 | -41.5566 | 2026-08-14 01:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 220.5 |
| f3252968-bc9f-350c-89ec-fc83494323fb | -21.9054 | -55.3538 | 2026-08-14 01:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4b40b99a-6e58-3c9e-82f5-20f644d50e0a | -15.1688 | -52.8241 | 2026-08-14 01:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 266310cc-ca3d-31b4-a29e-4efc03779e42 | -15.0924 | -48.649 | 2026-08-14 01:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d01774b3-b322-339c-b599-786e9c3dcca0 | -4.4869 | -42.5336 | 2026-08-14 01:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| ed68864d-b716-3f4c-b8d2-ab37946decb1 | -11.5074 | -54.6256 | 2026-08-14 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 04d70cb6-cf8f-3ece-bb48-1ba4c30befbe | -6.6195 | -59.0416 | 2026-08-14 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 2a18ae03-12c2-3107-a083-7f98d1ebf680 | -6.6194 | -59.0609 | 2026-08-14 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 04e58f80-c365-3455-8852-114775af1f48 | -15.1559 | -41.5566 | 2026-08-14 01:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| b895cb3d-f68e-3920-a70b-0e26c9ecf79a | -11.5074 | -54.6256 | 2026-08-14 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0bcfb034-ddf4-39f1-a427-e7b8c42b5ef4 | -21.9054 | -55.3538 | 2026-08-14 01:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 341630cc-4432-32f1-94ea-80652972c5d0 | -4.5057 | -42.5325 | 2026-08-14 01:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| baef68a8-e984-36a4-8f29-d6d6d0528dd7 | -14.4734 | -45.6914 | 2026-08-14 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| e41f6f33-7bb4-3d28-9f14-d92bcd635bbf | -21.9049 | -55.3755 | 2026-08-14 01:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 109.4 |
| da5a16bc-4769-3a9c-9cc8-2a3f2627ce86 | -13.5701 | -46.2584 | 2026-08-14 01:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 45836a52-c7c6-3fb0-ae46-6252546daa59 | -4.5055 | -42.5561 | 2026-08-14 01:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 179.7 |
| 40bab685-950a-30ad-95bc-2a24d7c265c3 | -11.4887 | -54.6068 | 2026-08-14 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e5170955-10ff-397a-9b52-8582eee56354 | -11.4885 | -54.6273 | 2026-08-14 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| de963a04-8931-350f-9f7c-4f44a5261aa7 | -6.9145 | -43.6351 | 2026-08-14 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 3705f503-a6be-3101-8b26-3377c6e0bdd5 | -4.4869 | -42.5336 | 2026-08-14 01:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 2b24c56d-6ceb-3138-a383-91ab619e3641 | -6.6195 | -59.0416 | 2026-08-14 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 05b18332-660b-38e5-bbc1-0e4f55d463a6 | -13.2413 | -54.2683 | 2026-08-14 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2f7772f2-f359-317d-9b69-97f50fcc9c73 | -4.4868 | -42.5572 | 2026-08-14 01:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 77f48f01-0012-31e7-b652-9bdc613be191 | -15.1368 | -41.536 | 2026-08-14 01:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.7 |
| 6eaf1e37-6d9b-37e9-b50d-a87d8fb89042 | -13.2415 | -54.2476 | 2026-08-14 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 88324569-a2a4-35d1-a49f-07f0ca69ff42 | -15.1362 | -41.561 | 2026-08-14 01:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 145.4 |
| f98f6493-c303-31ab-a923-298c0838b27f | -15.1688 | -52.8241 | 2026-08-14 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5af3c965-1c5e-341c-a7e9-43dabc784003 | -11.5076 | -54.6051 | 2026-08-14 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7b442cee-aaec-36ab-940a-060e95a17a1d | -6.6194 | -59.0609 | 2026-08-14 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8006608b-72d6-3baa-8d0e-3e5e21e2cee2 | -15.13 | -41.58 | 2026-08-14 01:15:00 | MSG-03 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 887e8418-f8c3-346d-8b62-e6bc7a7b7535 | -4.49 | -42.57 | 2026-08-14 01:15:00 | MSG-03 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f5ce734-897c-33f5-b99a-234479163f1e | -4.49 | -42.53 | 2026-08-14 01:15:00 | MSG-03 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bdac8bc6-77c5-39c3-af87-61f1c25e2579 | -21.9049 | -55.3755 | 2026-08-14 01:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 115.2 |
| bb1d999e-bcdc-3511-a938-b97477d33a5c | -11.5074 | -54.6256 | 2026-08-14 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 78b1626b-b6f6-3899-88e9-2ce2bda07e54 | -13.2415 | -54.2476 | 2026-08-14 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 1747a070-867b-3393-856d-365d6cc8ffd4 | -4.4868 | -42.5572 | 2026-08-14 01:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| c4aa6ecc-1619-383f-9d35-97fa0ca3b5a7 | -13.2413 | -54.2683 | 2026-08-14 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2b5e9d9d-68fc-31cb-879b-98b5e22b531f | -15.1362 | -41.561 | 2026-08-14 01:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 132.3 |
| 54f2fe69-290f-3b88-b468-fcaf71216a80 | -15.0924 | -48.649 | 2026-08-14 01:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 48831737-5395-369d-ae35-495d008ad0d6 | -14.4734 | -45.6914 | 2026-08-14 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 30c54a4b-5c0c-33e8-a378-235886e88ef3 | -11.4885 | -54.6273 | 2026-08-14 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 94c15c19-2e40-338d-aff0-2bea91cea57e | -16.9191 | -54.1481 | 2026-08-14 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 69160215-3577-3907-a38e-18c068b712fe | -15.1688 | -52.8241 | 2026-08-14 01:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 2233f475-7b29-3982-b886-12580fb5f4e3 | -13.5507 | -46.2615 | 2026-08-14 01:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 9cce20ce-538b-315e-ad89-dd11d38fde82 | -16.9195 | -54.127 | 2026-08-14 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a62dc87b-1e00-33d3-9f56-3bb73b0dbfbc | -4.5055 | -42.5561 | 2026-08-14 01:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 186.8 |
| 5307fe55-3057-37c9-9df9-827e00c951a3 | -16.9387 | -54.1454 | 2026-08-14 01:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5ea74e4c-fef1-33f6-a0c2-80b0fca90018 | -21.9054 | -55.3538 | 2026-08-14 01:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 7ccf1e7d-c342-3317-8ae3-eff7e48d4a06 | -4.5057 | -42.5325 | 2026-08-14 01:20:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 167.9 |
| 2ab41644-f57b-3197-87a7-ac2baeb7fa98 | -6.9145 | -43.6351 | 2026-08-14 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |


[Clique aqui para ver as próximas entradas](README6.md)
