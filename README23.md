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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddf5a15c-32c5-3338-8b96-92704d03360b | -11.94857 | -58.75121 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5ebb2c0-b1ae-361e-a8f0-cbf6856d8bd4 | -14.22967 | -45.51735 | 2025-06-21 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2df8ff64-76f4-385f-892d-f1a1e01e2f18 | -12.29027 | -50.10844 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f428be6-21b8-3669-bccf-4bc3c75f1592 | -13.09656 | -52.29928 | 2025-06-21 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddde25f1-aea5-327c-bb86-a143a6aca765 | -12.12921 | -54.66724 | 2025-06-21 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e25e7f7-f2fa-3a65-abd9-dd6674e3005c | -12.16519 | -48.67906 | 2025-06-21 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4e0778d-3807-3682-911d-ab226a5dce07 | -11.86959 | -52.25372 | 2025-06-21 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f4944be-dba6-3091-adf6-7cff61367c69 | -12.57552 | -58.37561 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c8aa7de-9ff4-3a28-8780-ec9cc5f57793 | -11.94204 | -58.7457 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff07e7e2-2505-386c-a2b9-070ab4fe21ba | -12.05991 | -63.78095 | 2025-06-21 05:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 095eb4ed-0a79-3675-b1b9-ee20cd960abf | -12.89241 | -56.98413 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee4b8715-6aa7-33cc-aa81-6769f31668cb | -13.04676 | -53.71276 | 2025-06-21 05:01:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4d4789e-d322-32d4-a540-2e2b92507964 | -11.57494 | -54.56578 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b67f25d8-f65a-3754-8bfb-c5f800686d96 | -10.23656 | -64.36099 | 2025-06-21 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9324e5e-0bd7-391e-a895-0a8fcc126d80 | -12.4673 | -57.18917 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40e167d5-0892-3d04-8fde-096d355f3b83 | -11.95438 | -58.76101 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a91b0adb-fcb9-3c66-b057-db48bc11a641 | -11.18469 | -54.40195 | 2025-06-21 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 172a4034-3b22-36a2-9274-19e9f4b52b8d | -12.28664 | -50.10403 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c7310d2-55ca-318b-abda-82cb70de936b | -10.89135 | -56.46002 | 2025-06-21 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 794f9498-bc32-37eb-b4db-a4ca68ed8170 | -12.5469 | -48.49955 | 2025-06-21 05:01:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4d59674-151b-3ec9-bed1-ce5eee37e9ef | -12.45311 | -57.19057 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cbe2658-de8d-3b34-85d6-27199bcea094 | -11.57104 | -54.56882 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92b12bec-6e8a-38be-841e-5bdad00b559c | -10.23721 | -64.35763 | 2025-06-21 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b7fb2b-4c08-380c-9ba4-e930ff1e2ddb | -11.958 | -58.76174 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d38fc0f1-73ae-3c42-96c0-b2c6e6607aab | -12.58092 | -56.98474 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0baf70d-9718-31ef-a47a-2d4d1a215a46 | -12.88567 | -56.983 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e252c715-ae5b-3a20-bbb5-1d621f0df79a | -12.02874 | -57.09385 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eab4af74-0b22-375c-ba71-02c810ad44a0 | -10.88798 | -56.45947 | 2025-06-21 05:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 829a74bb-e574-3d9c-80cc-856349180ee1 | -12.50897 | -58.34464 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d79e49b-30a8-3848-8993-c7bc56369867 | -12.444 | -48.14233 | 2025-06-21 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4000718-755f-3d56-aa35-d8e5f9e9aa4f | -11.78755 | -57.24467 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fff23309-99af-309d-bae0-eebe1fa4d49d | -11.87867 | -54.67596 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4d25eedd-5fd7-3f10-ae51-8599e4600daa | -12.02753 | -57.10127 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3d60bc1-fbc8-3f6f-b493-85ea6c57b67d | -12.57417 | -58.38371 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1d75710-bd9f-3722-bba5-ec0f2ef99b91 | -12.97618 | -54.68291 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b32b5ed-793f-3ba9-a463-be9c4ac28744 | -12.02813 | -57.09756 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da4f1ae6-3d93-3165-8ea0-da08b60e4946 | -11.87477 | -54.679 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 65b2a014-6ea9-3b98-8ec8-96a7d4bdfd4e | -12.47584 | -54.42305 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5e727372-a6d2-37a0-8321-4f7e06095f6a | -11.95511 | -58.75673 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f3069135-f0f3-32c2-ba3b-6b1b8a89a18f | -11.87922 | -54.67239 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 1ea55ef8-cd86-3e9e-b5ec-c39c1ee6f4ea | -13.23619 | -49.84087 | 2025-06-21 05:01:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 073e2a2e-c1c2-394b-a73d-78f8ca938eff | -11.61781 | -58.29519 | 2025-06-21 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28ae1d61-9aea-3f4a-9adb-4efb307017d2 | -13.36582 | -54.25968 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ebba092-eae9-3d72-8f91-a7dbb492536d | -12.13256 | -54.66777 | 2025-06-21 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1a78795-a229-39c8-bb84-bc6e40336dc5 | -11.95001 | -58.74272 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fbd8018-ebf6-31db-8da5-152f782d3315 | -12.88904 | -56.98357 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 091a76ef-39cd-3f1b-ab18-2e6ad9cf43b1 | -11.52976 | -56.98132 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82efa8d1-3c2f-36a1-a0bb-484df12953a4 | -13.29169 | -57.0873 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d16008-d63f-33b7-88d4-0079686e88de | -12.16457 | -48.68372 | 2025-06-21 05:01:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4aae5a4-7ce0-3469-be51-24bfa3d602c1 | -14.22354 | -45.51859 | 2025-06-21 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4509f8ef-a68a-39eb-bd23-87c9dd357f06 | -11.95076 | -58.76035 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f397fd06-bffb-3237-a5df-71a62d81dcd9 | -11.79097 | -57.24526 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 97552605-b878-3e1e-9a1b-044f9ea01f83 | -14.02586 | -53.3662 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9972f652-b7e4-3137-b586-bfaf1eca9ba6 | -11.88312 | -54.66936 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 01238410-bea0-3baa-911d-9f86c175f5fe | -13.36639 | -54.25596 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a98b1c3-f1ae-38e7-aaec-7a191a4ac948 | -15.07631 | -48.94605 | 2025-06-21 05:01:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f69e9723-b748-3791-83da-46836482a529 | -12.47191 | -54.42614 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad098e3c-e053-3f25-a31c-d67dc0a717aa | -11.94059 | -58.75424 | 2025-06-21 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82f6da79-e8a6-301a-88fb-09b02ecfac2d | -12.47921 | -54.42358 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 76b8ae57-6335-3cf3-ab36-b0e40004d491 | -12.02934 | -57.09014 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b2e0e2f-70d0-3f4b-a79b-5b03a6f813da | -12.28232 | -57.27212 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f3966f7-06f9-3cdb-bc90-4dfacfea565f | -14.03352 | -53.36326 | 2025-06-21 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 140e3e00-fcd9-3fdc-8e5e-15be1434fb29 | -11.36671 | -56.56413 | 2025-06-21 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 836f4f74-af94-3342-9093-727d82165304 | -14.81057 | -48.4767 | 2025-06-21 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43304248-85df-372e-b3b5-d364fbcecff6 | -11.53435 | -56.97451 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27596112-ad22-3fb1-b789-a92103a9e3c7 | -12.02594 | -57.08958 | 2025-06-21 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0368cba1-eea8-3fa2-a335-2c914025e3a1 | -11.87309 | -54.66776 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7f76baa7-35df-3736-8fc3-ba2d12d66e3b | -11.92065 | -54.8174 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 665bc65e-dbcf-3947-9ede-9d62734910f1 | -12.28197 | -50.10724 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd1be710-fe86-3fdf-9314-dd9876ffd8e5 | -12.58033 | -56.98839 | 2025-06-21 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5487b14-966c-3566-bd4d-dadc5511a264 | -11.52815 | -56.96969 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfaf7e79-a9e8-3cc6-a180-94874e228a3c | -10.77593 | -58.45992 | 2025-06-21 05:01:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daffc9e4-21b4-3142-93c9-c500302ba6f8 | -13.14772 | -56.80996 | 2025-06-21 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0195c16-6e21-3c0b-b638-68e2e0525fba | -12.28716 | -50.10021 | 2025-06-21 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a78251ea-f48d-3111-ac06-8beff43d13c9 | -11.91731 | -54.81686 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76d5f102-c8d5-36d8-a33e-0c8ec4a66f23 | -12.97226 | -54.68599 | 2025-06-21 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15803bdd-5f93-3955-9f3b-7d2610f24763 | -11.87198 | -54.6749 | 2025-06-21 05:01:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20ce26d7-68c3-3fa9-9661-22d68f6a683d | -11.57549 | -54.56221 | 2025-06-21 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d23b7ad7-06ac-3c81-b498-b7f9203220c4 | -11.78536 | -57.23659 | 2025-06-21 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| fd08e940-fe73-3736-b238-eccbbd9f4388 | -21.17697 | -48.69355 | 2025-06-21 05:04:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b225163e-39b2-34df-97d1-b6ebe594d133 | -25.56722 | -49.36703 | 2025-06-21 05:04:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 20dbb160-be1e-30ed-9615-82e22b7c6bd5 | -21.68867 | -49.50438 | 2025-06-21 05:04:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| bee99f67-56ba-32f7-994b-352a96151734 | -21.08504 | -55.77191 | 2025-06-21 05:04:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad84a50d-7a49-3213-950f-da7947c40f6e | -19.37156 | -51.40654 | 2025-06-21 05:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf2863cb-0908-319e-ae02-b433f4808eeb | -19.37209 | -51.40245 | 2025-06-21 05:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3219dd89-dfbc-391d-a6ef-74b6381872dd | -21.68929 | -49.49864 | 2025-06-21 05:04:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8b9e02f5-7661-316d-a044-0660a1e740fe | -21.44492 | -54.5744 | 2025-06-21 05:04:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4345621-57d7-3033-b53e-d0447c133b96 | -19.3754 | -51.40636 | 2025-06-21 05:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3d25109-b533-3a73-97f1-fc3be21c5dac | -21.17556 | -48.69537 | 2025-06-21 05:04:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a12da273-f24c-3dcf-a350-d5bdf19a9012 | -21.13156 | -56.23378 | 2025-06-21 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fe87e7b-deea-3b46-8482-c9a6fd180102 | -19.37118 | -51.40585 | 2025-06-21 05:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e491c636-7b35-3d5a-869b-8909fcc192fc | -21.01576 | -52.82206 | 2025-06-21 05:04:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 683ce1f5-3f1e-314d-86ad-49b8bcb1870e | -24.24309 | -50.7409 | 2025-06-21 05:04:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d08fc7d4-2d70-368a-bfc4-92fafe4eaac7 | -21.44131 | -54.57384 | 2025-06-21 05:04:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e1bdac6-ae35-3226-860b-a9a2453073ba | -22.94313 | -43.30815 | 2025-06-21 05:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 67f2e3e4-f43e-3572-9a09-47f6381ffea7 | -21.1759 | -48.69219 | 2025-06-21 05:04:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 260bf42e-d7c2-32c9-a141-1cf74db04fa3 | -21.02832 | -55.63788 | 2025-06-21 05:04:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e691e270-a2cd-39dc-b27b-1def307aa4b8 | -21.12817 | -56.23319 | 2025-06-21 05:04:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aedbc5af-b85a-3f01-9b2b-cb32fd4d84c9 | -21.01626 | -52.82606 | 2025-06-21 05:04:00 | NPP-375D | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 520b6130-326f-3973-b54a-6fdcdc8aa139 | -21.17664 | -48.69675 | 2025-06-21 05:04:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
