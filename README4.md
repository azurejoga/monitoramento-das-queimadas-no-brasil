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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5be316d-172f-362b-89a7-ff0a961641d2 | 3.73653 | -60.91909 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3270bf88-e3f6-31cd-853c-9509aa4c69c7 | 4.20368 | -60.89594 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 836cd054-2976-3fd7-a525-0459c488ccae | 3.73597 | -60.91561 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71b17fa-f17c-3b3c-8661-c0f9c93550f2 | 3.12229 | -60.31264 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d98689e-54bc-3862-93f2-e7f84aa3f929 | 3.88061 | -61.03518 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8aab342e-6a0b-328c-9d8d-54c77102abe5 | 2.23773 | -60.70599 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d2ccb72-aadf-3278-8a1a-413f62334f2f | 4.34371 | -61.0084 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f029c00-1519-34c2-9f35-16629d77c545 | 3.83906 | -61.00614 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 064566fe-8ff2-3518-88cc-252339becacd | 1.94954 | -60.78305 | 2026-02-14 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c64581a-5220-3192-bf03-d669eee9964d | 2.54453 | -61.25296 | 2026-02-14 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d3c25a0-6801-3248-883e-61c5f2173683 | 3.23867 | -60.19123 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce52c8b5-58ea-3c26-bc21-74343fdcee48 | 3.84797 | -60.91583 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1cb2366-e565-3643-a6b2-047c27887966 | 2.23716 | -60.70245 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7d976749-192f-36b7-8f9c-0bc8890bebe2 | 3.7393 | -60.91509 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd2bf6ac-5051-3a9f-8d5d-a01b7e972109 | 3.83961 | -61.00961 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ebd0872-296b-3fe5-8aba-6788cf2aa651 | 3.87674 | -61.03225 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cb54a1f-ab43-3645-a629-96b8a0a50a01 | 3.72876 | -60.93457 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 187c74cd-c1c8-3733-bcaf-9a1b05726ede | 3.11159 | -60.31067 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 008a6e53-ae10-3ae9-b82b-21540092456d | 3.83683 | -61.0136 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6dd5f11-6bd3-3d82-bc04-8b69636e7861 | 3.88007 | -61.03173 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b9866bc-fc9f-3167-a3fd-4354a4df0d9e | 2.2338 | -60.70298 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8990751-6aa7-3ba9-908c-690b34344ebd | 3.86844 | -61.0229 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26a77ca3-4190-3607-8158-caf7490658c2 | 3.81905 | -60.69178 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49f49fcc-2113-3f27-a215-8a41932014e8 | 3.18835 | -61.25826 | 2026-02-14 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aad6af4-444d-3215-b574-a7bfe0447f1e | 3.87564 | -61.02533 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9294bd04-9887-3f0a-a040-1d079efe004a | 3.75263 | -60.89161 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5310bc2-eebe-3d00-9be0-067d716b5eed | 3.83631 | -60.92835 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a87d1f78-8d7a-340e-bcb8-80803c02cfac | 1.83922 | -60.83642 | 2026-02-14 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83263e51-5dc8-38ef-af82-285e8e819365 | 1.83586 | -60.83694 | 2026-02-14 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d835c0d-5bb8-3991-9e36-5b49e02f5703 | 3.86899 | -61.02637 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a0355ba-223c-3f7a-9e94-0178dc69c6c2 | 3.10936 | -60.31836 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f4a02eb-662d-3943-8b65-3c41a8dc0c67 | 4.20091 | -60.89999 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc384be3-1b0f-3002-840f-b2525af3bc5f | 3.72713 | -60.93886 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c1c422a-85b9-3e20-940d-621a9c293f91 | 2.54731 | -61.24898 | 2026-02-14 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f429306-8053-361b-9949-3f9c4b569633 | 3.75597 | -60.89109 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8db597b0-d685-3ab0-9cff-1e17a5c705ab | 3.73375 | -60.92309 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bf4526b-5ce4-3fb8-bddc-b8bf57af93cd | 3.83793 | -61.02052 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84a764ed-a413-321f-86db-3c91bd1101f3 | 4.14906 | -60.11163 | 2026-02-14 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efc83364-4a10-31c2-8667-1dfb5c355e37 | 3.75041 | -60.89909 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaa9046c-dbfd-353c-8571-20859e0f2e6c | 3.80869 | -60.90064 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29015c54-927e-36fd-a35d-8ac3e06d0285 | 3.87952 | -61.02828 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60caad47-138b-3cbb-a732-29a54bf5e919 | 3.12287 | -60.31623 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba1a5e34-5521-3f02-9125-3b610aa219c0 | 3.67941 | -60.93924 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23c6078e-9eb0-33f3-9f56-633debb7115e | -9.23114 | -65.71608 | 2026-02-14 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f83b8609-71e9-3c74-a91e-16325de21f3f | -9.54142 | -64.06255 | 2026-02-14 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cb6f4e4-8fe6-371d-a320-55736600da88 | 3.1198 | -60.30614 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e8e923-c11f-39e7-98f5-c6fc161d4738 | 3.86895 | -61.02 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cb86ac5-27b3-38a9-94c5-fb191fa1cb48 | 3.73864 | -60.9156 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85164788-24e3-3304-8aa7-1474f2da4a85 | 3.84754 | -60.91986 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d58d94b-0f05-319b-bcc0-378924ee5eee | 3.74324 | -60.91486 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff8d4eba-f172-3fb7-b0ce-6c0d4b7f4103 | 3.11183 | -60.31843 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36a1b6bf-344e-3092-ba0f-6280eb7e6147 | 3.11096 | -60.3131 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1b0035a2-7a29-3f4a-b074-2fa519aee475 | 3.10909 | -60.31176 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1409da4d-2eb1-3bd3-97b4-c76b9fd59f53 | 3.83377 | -60.91976 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d97cc952-197f-3a3f-992a-719bce8f3df0 | 3.73562 | -60.92388 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c7dd692-6b7c-31e3-a09b-88d19265126c | 3.12452 | -60.31467 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c38d38c-6930-369a-a0cb-4c598f748a37 | 3.73867 | -60.91362 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffc4904b-6864-35a8-a89c-cd5008f70bdb | 3.73258 | -60.93417 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a1a48c6-a217-3a75-a8e4-aa328b0bf281 | 3.87516 | -61.0265 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f23a03b-dfb8-38ed-aa17-67394728e07d | 3.72877 | -60.93968 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 462ff123-9976-3d3d-940a-337ba2a1a302 | 3.88122 | -61.0346 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08d69f1b-ce11-35fc-a733-f160d1a231a2 | 2.23651 | -60.70189 | 2026-02-14 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ec7cd3f-f23c-3e99-9712-2ade66e6ace8 | 3.83529 | -60.929 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba20880d-766b-3af1-a061-69f73d77d818 | 3.83452 | -60.9243 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2a3204b-8d94-34fd-8012-7aaba76e651f | 3.73945 | -60.92033 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 679cad58-2a35-3ddb-a7d3-eabb7e8cd9db | 3.87963 | -61.02815 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13f3c4b3-5ea0-35e6-b873-4ffa515e39b9 | 3.86972 | -61.02475 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aeb204c-51c0-3dec-ba89-0e3661f373db | 3.86978 | -61.02243 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 629d5a22-0a98-3ad9-9552-e785b3592af5 | 3.74243 | -60.91013 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad17ef83-8d65-3e64-be98-21d58b13afe8 | 3.8805 | -61.03039 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 426090a9-d25b-3f47-9f2c-080b947a1d15 | 3.7425 | -60.90812 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eba84229-bd07-343b-8dea-73b24287ae91 | 3.7318 | -60.9294 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4547f00-0cfb-3b42-b9d3-e0867ff7f098 | 3.10999 | -60.31706 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6400bab-2493-348b-8aaf-8780eee46003 | 3.75399 | -60.89154 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a6bdc0-0421-3a62-90d2-006ab1e2bbdc | 1.83648 | -60.83719 | 2026-02-14 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03cbfebe-bff2-357a-9be5-8066212f4ed6 | 3.88034 | -61.03253 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0f0c4c2b-5533-36c4-a392-69559acff570 | 3.73944 | -60.91835 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c32a1b53-b671-3138-b465-e7aa8f183cce | 3.84751 | -60.91726 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4d9f992-77b7-36fe-9aa2-d4dc8d529fc9 | 3.75381 | -60.89362 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38729e6b-564e-3fcd-8cbb-eba0ba664cfb | 2.23735 | -60.70704 | 2026-02-14 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b607e417-6517-3de4-ac85-5f187cdcf6c9 | 3.11394 | -60.31095 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 694d8b95-086e-31e5-976e-6e763433958d | 3.11788 | -60.30484 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dcbed70-0ac0-3d4c-af8e-d80de8c20718 | 3.81816 | -60.69249 | 2026-02-14 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b12311b-c43c-3782-b41c-34785ad64d03 | 3.87434 | -61.0217 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfdd31d-a303-3959-8417-f64f2b832e9f | 3.84369 | -60.92273 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 083b685f-b1a8-3585-a75b-b4c6302c6f27 | 3.87884 | -61.02327 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bccd809-6d98-3d36-a064-933c84622790 | 3.84674 | -60.91517 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8219d23e-e903-380c-8bcd-9ee803d0f64a | 3.75016 | -60.89709 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe1d82c7-d3e9-3989-82bf-643764a2dfe9 | 3.74623 | -60.90467 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e892aab0-0e68-3b9e-9ffd-c195345e8482 | 3.11581 | -60.31229 | 2026-02-14 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bf018ee-a0ee-3a20-b9cc-2ff43e4221b3 | 3.74633 | -60.90263 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba3a32aa-1a56-3902-a05c-289c47ac336c | 3.75002 | -60.89915 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3be16821-7509-3e8f-b890-4e38ae42257d | 1.83564 | -60.83203 | 2026-02-14 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fd868ae-1548-3361-a454-35b00bb96b63 | 3.87429 | -61.02407 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2608c3fe-e033-3011-9114-948e2e7e8c76 | 3.74327 | -60.91286 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4433f4d9-7b87-309a-b62f-9625d593ecd8 | 3.87971 | -61.02573 | 2026-02-14 05:59:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50bbef93-e819-3b86-babe-68cde0d19f05 | 4.20648 | -60.89768 | 2026-02-14 06:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b4bd99b-8677-3b35-96c7-cac3cb368021 | 4.20206 | -60.8993 | 2026-02-14 06:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c396a4b-a3d4-3b95-9e4d-473aeb79b755 | 3.73726 | -60.91422 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d20cd445-8148-3fd3-9420-a323bb2da777 | 3.73099 | -60.93443 | 2026-02-14 07:09:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README5.md)
